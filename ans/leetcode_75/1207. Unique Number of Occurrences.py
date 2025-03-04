class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ret_dict = {}
        for i in arr:
            if i not in ret_dict:
                ret_dict[i] = 0
            ret_dict[i] += 1
        return True if len(ret_dict.keys()) == \
            len(set([v for k,v in ret_dict.items()])) else False