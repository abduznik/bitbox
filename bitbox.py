import sys
import os
import importlib.util
import inspect

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")


def discover_tools():
    tools = {}
    if not os.path.isdir(TOOLS_DIR):
        return tools
    for filename in os.listdir(TOOLS_DIR):
        if filename.endswith(".py") and not filename.startswith("_"):
            name = filename[:-3]
            filepath = os.path.join(TOOLS_DIR, filename)
            tools[name] = filepath
    return tools


def load_tool(filepath):
    spec = importlib.util.spec_from_file_location("tool", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_description(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# description:"):
                    return line.split(":", 1)[1].strip()
                if not line.startswith("#") and line != "":
                    break
    except Exception:
        pass
    return "No description"


def list_tools(tools):
    if not tools:
        print("No tools found.")
        return
    print(f"\n  {len(tools)} tools available\n")
    print(f"  {'Tool':<25} {'Description'}")
    print(f"  {'----':<25} {'-----------'}")
    for name in sorted(tools):
        desc = get_description(tools[name])
        print(f"  {name:<25} {desc}")
    print()


def main():
    tools = discover_tools()

    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python bitbox.py <tool_name> [args...]")
        print("       python bitbox.py --list")
        print()
        print("Run 'python bitbox.py --list' to see available tools.")
        sys.exit(0)

    if sys.argv[1] == "--list":
        list_tools(tools)
        sys.exit(0)

    tool_name = sys.argv[1]
    tool_args = sys.argv[2:]

    if tool_name not in tools:
        print(f"Error: tool '{tool_name}' not found.")
        print("Run 'python bitbox.py --list' to see available tools.")
        sys.exit(1)

    module = load_tool(tools[tool_name])

    if not hasattr(module, "run") or not callable(module.run):
        print(f"Error: tool '{tool_name}' does not have a callable run() function.")
        sys.exit(1)

    sig = inspect.signature(module.run)
    try:
        bound = sig.bind(*tool_args)
    except TypeError:
        params = list(sig.parameters.keys())
        print(f"Error: tool '{tool_name}' expects {len(params)} argument(s): {', '.join(params)}")
        print(f"Usage: python bitbox.py {tool_name} {' '.join('<' + p + '>' for p in params)}")
        sys.exit(1)

    try:
        result = module.run(*tool_args)
        print(result)
    except (IndexError, TypeError):
        print(f"Error: wrong number of arguments for '{tool_name}'.")
        print(f"Usage: python bitbox.py {tool_name} <args...>")
        print(f"Check the tool file for expected arguments: tools/{tool_name}.py")
        sys.exit(1)
    except Exception as e:
        print(f"Error running tool '{tool_name}': {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
