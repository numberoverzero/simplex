import re


ESCAPE = "\\"
REFERENCE = "(?P<{name}>{match})"
BACKREF_SYNTAX = re.compile("ref\((?P<name>.*?)\)")
BACKREF = "(?P={name})"
STATES = [
    "START",
    "CONSTANT",
    "MATCH",
    "ERROR"
]


def _build_const(match):
    return re.escape(match)


def _build_match(match):
    pieces = match.split(":")
    if len(pieces) == 1:
        return REFERENCE.format(name=pieces[0], match=".*?")
    elif len(pieces) == 2:
        m = BACKREF_SYNTAX.match(pieces[1])
        if not m:
            raise ValueError("Unknown constraint " + pieces[1])
        return BACKREF.format(**m.groupdict())
    else:
        raise ValueError("Unknown match " + match)


def compile(string):
    state = "START"
    parts = ["^"]
    context = ""
    error = None

    i = 0
    n = len(string)
    while i < n:
        c = string[i]

        if c == "[":
            if state == "START":
                state = "MATCH"
                i += 1
            elif state == "MATCH":
                state = "ERROR"
                error = "Cannot nest matches"
            elif state == "CONSTANT":
                if context[-1] == ESCAPE:
                    context += c
                    i += 1
                else:
                    parts.append(_build_const(context))
                    context = ""
                    state = "MATCH"
                    i += 1
        elif c == "]":
            if state == "START":
                state = "ERROR"
                error = "Unexpected match close"
            elif state == "MATCH":
                if context[-1] == ESCAPE:
                    state = "ERROR"
                    error = "Cannot nest matches"
                else:
                    parts.append(_build_match(context))
                    context = ""
                    state = "START"
                    i += 1
            elif state == "CONSTANT":
                if context[-1] == ESCAPE:
                    context += c
                    i += 1
                else:
                    state = "ERROR"
                    error = "Unexpected match close"
        else:
            if state == "START":
                state = "CONSTANT"
            context += c
            i += 1

        if state == "ERROR":
            break

    # Clean up last state
    if state == "START":
        pass
    elif state == "MATCH":
        state = "ERROR"
        error = "Missing expected match close"
    elif state == "CONSTANT":
        parts.append(_build_const(context))
        context = ""
        state = "START"
    parts.append("$")

    # Raise on errors
    if state == "ERROR":
        raise ValueError(error)

    uncompiled = "".join(parts)
    return re.compile(uncompiled)
