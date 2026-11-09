class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}                        # all the boxes (none yet)
        for word in strs:                  # take each word one by one
            key = "".join(sorted(word))    # find its label
            if key not in groups:          # no box with this label?
                groups[key] = []           #   make a new empty box
            groups[key].append(word)       # drop the word into its box
        return list(groups.values())       # empty out all the boxes
                