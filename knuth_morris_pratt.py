def make_failurelinks(pattern):
    failure_links = []
    j = 0
    for i, character in enumerate(pattern):
        if i == 0:
            failure_links.append(0)
        else:
            j = failure_links[i-1]
            if pattern[i] == pattern[j]:
                failure_links.append(failure_links[i-1]+1)
            else:
                failure_links.append(0)
    return failure_links

def find_pattern(string, pattern, failure_links):
    j = 0
    i = 0
    while i < len(string) - 1:
        while j < len(pattern):
            if(string[i + j] == pattern[j]):
                j += 1
            else:
                j = failure_links[j]
                break
            if(j == len(pattern) - 1):
                print("pattern found")
                return
        i += 1
    print("pattern not found")
    return


if __name__ == '__main__':
    failure_links = make_failurelinks("aac")
    print(failure_links)
    find_pattern("aaac", "aac", failure_links)
