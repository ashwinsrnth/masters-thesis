for img in *.svg
do
    echo convert $img ${img%.svg}.eps
    convert $img ${img%.svg}.eps
done
