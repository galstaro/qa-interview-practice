def is_palindrome1(s: str) -> bool:
    bad_chars = "!@#$%^&*(),.-'?\":{}|<>"
    for char in bad_chars:
        s = s.replace(char, "")
    s = s.upper().strip().replace(" ","")
    return s == s[::-1]



def is_palindrome2(s: str) -> bool:
    left = 0
    right = len(s)-1
    while left<=right:
        if s[right].isalnum() and s[left].isalnum() and s[left].upper()!=s[right].upper():
            return False
        if s[right].isalnum() and s[left].isalnum() and s[left].upper()==s[right].upper():
            left+=1
            right-=1
            continue
        if not s[left].isalnum():
            left+=1
        if not s[right].isalnum():
            right-=1
    return True               


def word_count(text: str) -> dict[str, int]:
    bad_chars = "!@#$%^&*(),.?\":{}|<>"
    for char in bad_chars:
        text = text.replace(char, "")
    text = text.split()
    d = {}
    for s in text:
        if s.lower() not in d:
            d[s.lower()] = 0
        d[s.lower()] +=1
    return d
        

def first_unique_char(s: str) -> str | None:
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c]+=1
    for x in d:
        if d[x] == 1:
            return x
    return None



def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    seen = {}
    for i in range(len(nums)):
        if target-nums[i] in seen:
            return (seen[target-nums[i]],i)
        else:
            seen[nums[i]] = i
    return None
            


def is_balanced(s: str) -> bool:
    d = {"(":")","{":"}","[":"]"}
    seen = []
    for c in s:
        if c in d:
            seen.append(c)
        if c in d.values():
            if len(seen) > 0 and d[seen[-1]] == c:
                seen.pop(-1)
            else:
                return False
    # removed == 0
    return len(seen)


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    c = []
    ia = 0
    ib = 0
    while ia < len(a) and ib < len(b):
        if a[ia]<=b[ib]:
            c.append(a[ia])
            ia+=1
        else:
            c.append(b[ib])
            ib+=1
    if ia == len(a):
        c.extend(b[ib:])
    if ib == len(b):
        c.extend(a[ia:])
    return c


def analyze_log(path: str) -> dict:
    d = {}
    with open(path) as f:
        for l in f:
            l = l.split()
            if len(l)>2:
                if l[2] not in d:
                    d[l[2]] = 0
                d[l[2]]+=1
    return d



if __name__ == "__main__":
    print(is_palindrome1("A man, a plan, a canal: Panama"))
    print(is_palindrome2("A man, a plan, a canal: Panama"))
    print(word_count("The cat and the hat."))
    print(first_unique_char("swiss"))
    print(two_sum([2, 7, 11, 15], 9))
    print(is_balanced("{[()]}))"))
    print(merge_sorted([1, 3, 5], [2, 4, 6]))
    print(analyze_log("f1.txt"))
            
