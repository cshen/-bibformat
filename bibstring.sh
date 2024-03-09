#!/usr/bin/env bash
#
# Chunhua Shen, 2016 June
#
# replacing abbreviations like ICCV with strings like "Proc. Int. Conf. Comp. Vis."
#


sfile='https://raw.githubusercontent.com/cshen/bibformat/main/cvml.bib'


sed=gsed

infile="$1"

[ ! -n "$1"  ]     && echo "An input bibtex file in needed." && exit 1
[ ! -f $infile   ] && echo "Abort. $infile not found. "      && exit 2


wget $sfile -O /tmp/cvml.bib


List=$(   \
    cat /tmp/cvml.bib  | $sed 's/@STRING{/  /' | grep -v EOF | grep -v \-  |   \
    grep -v USAGE: | grep -v bibliography   |  \
    $sed 's/=/   /' | awk '{  print $1  }' | $sed -e 's/^[ \t]*//g' | \
    awk 'NF'  \
    )

tmpf=/tmp/_temp.bib
cp -f $infile $tmpf

for s in $List
do
   echo '  replacing: '$s
   cat    $tmpf   |  $sed "s/{$s}/$s/Ig" > /tmp/_temp1
   sleep 0.01
   mv -f /tmp/_temp1 $tmpf
done

cat /tmp/cvml.bib   > /tmp/_temp2
echo "   "         >> /tmp/_temp2
cat $tmpf          >> /tmp/_temp2

fname=`echo $infile | cut -d'.' -f1`_2.bib

cp -i /tmp/_temp2 $fname

rm -f $tmpf
rm -f /tmp/_temp2

echo "Done. The processed bibtex file is: "$fname


