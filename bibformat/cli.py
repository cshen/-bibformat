"""Console script """
import sys
from bibformat import bibformat as bf



def main(args=None):

    if len(sys.argv) > 1:
        bibf = sys.argv[1]
        # print("The input bibtex file is: " + str(bibf) )

        print("% This bibtex is generated using https://github.com/cshen/bibformat   " +  x.strftime("%D %T"))
        print("% You will need to: wget https://raw.githubusercontent.com/cshen/bibformat/main/cvml.bib")
        print("")

        bf.format_bibtex( str(bibf) )
    else:
        print("Please input a bibtex file to process.")
    return 0




if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
