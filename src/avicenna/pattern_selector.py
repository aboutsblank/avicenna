# question: what do we need (input) must have?
# pattern catalogue (all patterns)
# current prominent features list
from enum import Enum
from typing import Set, Optional, List

from isla import language
from isla.language import Formula


# question: what would be nice to have?
# previously activated patterns
# previously prominent features

# question: what do we output?
# list / set of all activated patterns

# ideas to solve the problem
# first cycle run all patterns and only get specific later on

class SelectionMode(Enum):
    ALL = "ALL"
    BY_FEATURE = "BY_FEATURE"

# aim: PatternSelector manages the patterns for avicenna, in all other places only active patterns should be present
# option 1: PatternSelector has sole responsibility for patterns in Avicenna (data + methods)
# option 2: PatternSelector only provides functionality to select patterns according to specific modes
class PatternSelector:

    def __init__(
            self,
            selection_mode: SelectionMode,
            pattern_file: Optional[str] = None,
            patterns: Optional[List[Formula]] = None):
        self.selection_mode: SelectionMode = selection_mode
        self.patterns = patterns
        # self.correlated
        # self.excluded
        # self.relevant

    def select(self, relevant, correlated, excluded) -> Set[language.Formula]:
        # TODO refactor this
        match self.selection_mode:
            case SelectionMode.ALL: return self.all(relevant, correlated, excluded)
            case SelectionMode.BY_FEATURE: return self.by_feature_type(relevant, correlated, excluded)
        raise NotImplementedError


    def all(self):
        raise NotImplementedError


    def by_feature_type(self):
        # feature in features isinstance(ExistenceFeature)...
        # super Feature
        # ExistenceFeature
        # DerivationFeature
        # NumericFeature
        # LengthFeature
        # match top feature (first feature) type to pattern type (categorization of patterns needed)
        # count occurrence of feature types and then ratio patterns ?
        #
        raise NotImplementedError
