# from functions.get_files_info import get_files_info
# from functions.get_files_content import get_files_content
from functions.write_file import write_file


def test():
    # result = get_files_info("calculator", ".")
    # print("Results for current directory:")
    # print(result)
    #
    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)
    #
    # result = get_files_info("calculator", "/bin")
    # print("Results for '/bin' directory:")
    # print(result)
    #
    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)
    #
    # result = get_files_content("calculator", "lorem.txt")
    # print("Results: ")
    # print(result)

    # result = get_files_content("calculator", "main.py")
    # print("Result:")
    # print(result)
    #
    # result = get_files_content("calculator", "pkg/calculator.py")
    # print("Result:")
    # print(result)
    #
    # result = get_files_content("calculator", "/bin/cat")
    # print("Result:")
    # print(result)
    #
    # result = get_files_content("calculator", "pkg/does_not_exist.py")
    # print("Result:")
    # print(result)
    #

    result = write_file("calculator", "lorem.txt", "wait, this isnt lorem ipsum")
    print("Results: ")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Results: ")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Results: ")
    print(result)


if __name__ == "__main__":
    test()
