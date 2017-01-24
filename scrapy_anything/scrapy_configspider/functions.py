import re


def match_first(src, regex):
    if not regex:
        return src
    match = re.compile(regex).search(src)
    return match.group(min(1, len(match.groups()))) if match else ''
