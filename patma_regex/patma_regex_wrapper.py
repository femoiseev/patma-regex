import re


__patma_regexes__ = {}


def PatmaRegex(pattern, unanchored=False):
    """
    Creates class that can be used for destructive group matching of regex in match / case clause.

    Args:
        pattern (str or compiled regex): Used regex pattern
        unanchored (bool): Defines match condition: whole string (unanchored=False) or some substring in the middle (unachored=True)

    Returns:
        class suitable to use in match / case clause to extract groups defined in passed pattern from matched string.
    """
    if isinstance(pattern, str):
        pattern = re.compile(pattern)
    index_to_group = {v: k for k, v in pattern.groupindex.items()}
    
    class_name = f'PatmaRegex{id(pattern)}'
    match_args = [index_to_group.get(i + 1, f'group{i + 1}') for i in range(pattern.groups)]
    
    def init(self, *args):
        for group_name, arg in zip(self.__match_args__, args):
            setattr(self, group_name, arg)
    
    def match(s):
        if not isinstance(s, str):
            return None

        RegexPattern = __patma_regexes__[class_name]
        result = RegexPattern.pattern.search(s) if unanchored else RegexPattern.pattern.fullmatch(s) 

        if result:
            return RegexPattern(*result.groups())
        else:
            return None
 
    __patma_regexes__[class_name] = type(class_name,
                                         (),
                                         dict(
                                             __match_args__ = match_args,
                                             __init__ = init,
                                             __match__ = match,
                                             pattern = pattern
                                         ))
    return __patma_regexes__[class_name]
