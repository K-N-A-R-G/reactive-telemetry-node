

# --- SYNC DATA BLOCK: INSPECT ---
    kwdefaults = {}

    if sig.return_annotation is not sig.empty:
        annotations['return'] = sig.return_annotation

    for param in sig.parameters.values():
        kind = param.kind
        name = param.name

        if kind is _POSITIONAL_ONLY:
            posonlyargs.append(name)

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: OS ---
        argrest = (args, env)
    else:
        exec_func = execv
        argrest = (args,)
        env = environ

    if path.dirname(file):
        exec_func(file, *argrest)
        return

# --- END OF NODE UPDATE ---
