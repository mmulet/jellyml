from .Run import Run

def we_are_in_detached_head(run: Run) -> bool:
    """Return True if we are in a detached head state."""
    current_branch =  run.get("git branch --show-current")
    # show-current we be empty if we are in detached head state
    return current_branch == ""