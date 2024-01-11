def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        starting = s.find('src="') + 5
        ending = s.find('"', starting)
        final = s[starting:ending]
        change1 = final.replace('embed/','')
        change2 = change1.replace('be','')
        change3 = change2.replace('.com','.be')
        change4 = change3.replace('www.','')
        change5 = change4.replace('http','https')
        change6 = change5.replace('httpss','https')
        if not 'yout' in change6:
            return None
        elif not 'https' in change6:
            return None
        return change6
    except:
        return None



if __name__ == "__main__":
    main()
