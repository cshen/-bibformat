#!/usr/bin/env python3

import bibtexparser
import sys
from Levenshtein import distance
from Levenshtein import ratio

from bibformat import pre_process as p
import datetime



ICCV= ["Proceedings of the IEEE/CVF International Conference on Computer Vision"  ,
      "Proceedings IEEE/CVF International Conference on Computer Vision"  ,
      "Proc. IEEE/CVF International Conference on Computer Vision"  ,
      "Proc. IEEE International Conference on Computer Vision",
      "IEEE International Conference on Computer Vision (ICCV)",
      "Int. Conf. Comput. Vis.",
      "IEEE Conf. Comput. Vis." ]


CVPR= ["Proceedings of the IEEE/CVF International Conference on Computer Vision and Pattern Recognition" ,
       "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition",
"Proceedings IEEE/CVF International Conference on Computer Vision and Pattern Recognition" ,
"Proc. IEEE/CVF International Conference on Computer Vision and Pattern Recognition" ,
"Proc. IEEE International Conference on Computer Vision and Pattern Recognition" ,
"Int. Conference on Computer Vision and Pattern Recognition",
"IEEE Conference on Computer Vision and Pattern Recognition",
"IEEE Conference on Computer Vision and Pattern Recognition (CVPR)",
"CVF Conference on Computer Vision and Pattern Recognition"]


ECCV= ["Proceedings of the European Conference on Computer Vision" ,
       "Proceedings of the European Conference on Computer Vision (ECCV)",
"Proceedings Eur. Conference on Computer Vision" ,
"Proc. European Conference on Computer Vision" ,
"Proc. Eur. Conference on Computer Vision",
"Eur. Conf. Comput. Vis." ]


ACCV= ["Proceedings of the Asian Conference on Computer Vision" ,
"Proceedings Asian Conference on Computer Vision" ,
"Proc. of The Asian Conference on Computer Vision" ,
"Proc. Asian Conference on Computer Vision",
"Asian Conf. Comput. Vis." ,
"Proceedings of the Asian Conference on Computer Vision (ACCV)"]


ICML= ["Proceedings of the International Conference on Machine Learning" ,
       "Proceedings of the International Conference on Machine Learning (ICML)",
"Proceedings Int. Conference on Machine Learning",
"International conference on machine learning",
"Proc. International Conference on Machine Learning" ,
"Proc. Int. Conference on Machine Learning",
"Int. Conf. Mach. Learn."]


ICLR= ["Proceedings of the International Conference on Learning Representations" ,
"Proceedings Int. Conference on Learning Representations" ,
"Proc. International Conference on Learning Representations" ,
"Proc. Int. Conference on Learning Representations" ,
"Int. Conference on Learning Represent."]


AAAI= ["Proceedings of the AAAI Conference on Artificial Intelligence" ,
"Proceedings AAAI Conference on Artificial Intelligence"  ,
"Proc. AAAI Conference on Artifi. Intelli."  ,
"AAAI Conference on Artifi. Intelli."  ]


NeurIPS = [ "Advances in Neural Information Processing Systems",
"Proceedings Advances in Neural Information Processing Systems",
"Proceedings Int. Conf. Neural Information Processing Systems",
"Proceedings of International Conference on Neural Information Processing Systems",
"Int. Conf. Neural Information Processing Systems",
"Proceedings Adv. Neural Inform. Process. Syst.",
"Proceedings Int. Conf. Neural Inform. Process. Syst."]

KDD = [ "ACM SIGKDD Conference on Knowledge Discovery and Data Mining",
       "Proc. ACM SIGKDD Conference on Knowledge Discovery and Data Mining",
"SIGKDD Conf. Knowledge Discovery and Data Mining" ]


IJCV = ["International Journal of Computer Vision",
        "International Journal of Computer Vision (IJCV)",
        "Int. J. of Computer Vision"]

TPAMI = ["IEEE Transactions on Pattern Analysis and Machine Intelligence",
         "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)",
        "IEEE Trans.  Pattern Analysis and Machine Intelli."]

PR = ["Pattern Recog.",
      "Pattern Recogn.",
      "Pattern Recognition"]


arXiv= ["arXiv: arxiv",
        "arXiv preprint arXiv:"]

JMLR = ["Journal of Machine Learning Research",
        "Journal of Machine Learning Research (JMLR)",
        "J. Mach. Learn. Res." ]

TMLR = ["Transactions on Machine Learning Research",
        "Trans. Mach. Learn. Res."]

TOG =  ["ACM Trans. Graph.",
        "ACM Transactions on Graphics",
        "ACM Transactions on Graphics (TOG)"]



THRESHOLD = 15


# o = p.pre_process( CVPR[1] )
# print(o)


def replace_booktitle(s):

    dist = []
    ven  = []
    rat  = []
    o = p.pre_process(s)
    for v in ICCV:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'ICCV' )

    for v in ECCV:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'ECCV' )

    for v in ACCV:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'ACCV' )

    for v in CVPR:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'CVPR' )


    for v in ICML:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'ICML' )

    for v in ICLR:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'ICLR' )

    for v in AAAI:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'AAAI' )


    for v in NeurIPS:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'NeurIPS' )

    for v in KDD:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'KDD' )

    for v in IJCV:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'IJCV' )

    for v in TPAMI:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'TPAMI' )

    for v in PR:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'PR' )


    for v in arXiv:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'arXiv' )


    for v in JMLR:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'JMLR' )

    for v in TMLR:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'TMLR' )

    for v in TOG:
        v = p.pre_process(v)
        dist.append ( distance(o, v) )
        rat.append( ratio(o, v) )
        ven.append( 'TOG' )


    val_min = min(dist)
    idx_min = min(range(len( dist )), key=dist.__getitem__)

    rat_min = min(rat)
    idx_min_using_rat = min(range(len( rat )), key=rat.__getitem__)

    # print(val_min)
    # print( ven[ idx_min]  )
    # print()

    return s, ven[ idx_min], val_min, ven[ idx_min_using_rat ], rat_min



def format_bibtex( in_bibtex_f ):
# Load the BibTeX file
    with open( in_bibtex_f ) as bibtex_file:
        bibtex_str = bibtex_file.read()

        # Parse the BibTeX string
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.loads(bibtex_str, parser=parser)


# Print the parsed entries
        for entry in bib_database.entries:
    # print("Article:")
            string_dist = 1000
            string_ratio= 1

            print('@' + entry.get( 'ENTRYTYPE' ) +'{' + entry.get( 'ID' ) +',' )
            print('    author    = "' + entry.get( 'author' ) +'",' )
            print('    title     = "' + entry.get( 'title' ) +'",' )

            yr = str ( entry.get( 'year' ) or '')
            print('    year      = "' + yr +'",' )


            s = str ( entry.get( 'booktitle' ) or '')
            if not s == '':
                s, venue, string_dist, venue_ratio, string_ratio  =  replace_booktitle(s)

                if string_dist < THRESHOLD:
                    print('    booktitle = ' +  venue   +',' )
                else:
                    print('    booktitle = "' +  s   +'",' )

            s = str ( entry.get( 'journal' ) or '')
            if not s == '':
                s, venue, string_dist, venue_ratio, string_ratio  =  replace_booktitle(s)

                if string_dist < THRESHOLD:
                    print('    journal   = ' +  venue   +',' )
                else:
                    print('    journal   = "' + s +'",' )



            print('}')
                # print the original venue for checking
            if string_dist < THRESHOLD:
                    print("%  before replacement: " + s + "  " + str( string_ratio) )


            print('\n\n')


            # for key, value in entry.items():
            #    print(f"{key}: {value}")
            # print()

# Article:
# title: A Novel Approach to Image Composition
# author: John Doe
# journal: IEEE Transactions on Image Processing
# year: 2022
#


def main(args=None):

    x = datetime.datetime.now()

    if len(sys.argv) > 1:
        bibf = sys.argv[1]
        # print("The input bibtex file is: " + str(bibf) )

        print("% This bibtex is generated using https://github.com/cshen/bibformat   " +  x.strftime("%D %T"))
        print("% You will need to: wget https://raw.githubusercontent.com/cshen/bibformat/main/cvml.bib")
        print("")

        format_bibtex( str(bibf) )
    else:
        print("Please input a bibtex file to process.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        bibf = sys.argv[1]
        # print("The input bibtex file is: " + str(bibf) )
        format_bibtex( str(bibf) )
    else:
        print("Please input a bibtex file to process.")
