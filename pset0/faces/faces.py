def main():
    context = convert(input())
    print(context)

def convert(str):
    faces = str.replace(":)","🙂").replace(":(","🙁")

    return faces

main()
