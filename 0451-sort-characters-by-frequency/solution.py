from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        sorted_d_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        sorted_d = dict(sorted_d_items)
        st = []
        for key, value in sorted_d.items():
            st.append(key*value)
        return "".join(st)