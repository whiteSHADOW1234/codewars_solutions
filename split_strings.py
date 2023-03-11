def solution(s):
    ans = []
    if len(s) % 2 != 0:
        s = s +"_"
    
    while len(s) != 0:
        ans.append(s[:2])
        s = s[2:]
    return ans


def main():
    testcases = ["abc", "abcdef"]
    for testcase in testcases:
        print(solution(testcase))

if __name__ == "__main__":
    main()