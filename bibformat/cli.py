"""Console script """
import sys
import bibformat as bf



def main(args=None):

    if len(sys.argv) > 1:
        bibf = sys.argv[1]
        # print("The input bibtex file is: " + str(bibf) )
        bf.format_bibtex( str(bibf) )
    else:
        print("Please input a bibtex file to process.")
    return 0




if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
