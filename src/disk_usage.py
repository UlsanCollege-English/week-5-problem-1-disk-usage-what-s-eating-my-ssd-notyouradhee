
## Starter code — `src/disk_usage.py`

def total_size(node):
    """
    Compute total size of a nested file/dir tree.
    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}
    """
    # TODO: implement recursively
    if node and node.get("type") == "file":
        return node.get("size", 0)

    if node and node.get("type") == "dir":
        return sum(total_size(child) for child in node.get("children", []))

    return 0