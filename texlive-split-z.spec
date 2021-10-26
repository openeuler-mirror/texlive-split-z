%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-z
Version:        %{tl_version}
Release:        25
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Patch0108:      texlive-2017-xepersian-python.patch
Source0003:     texlive-licenses.tar.xz
Source0671:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xkeyval.tar.xz
Source0672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xkeyval.doc.tar.xz
Source0674:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcolor.tar.xz
Source0675:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcolor.doc.tar.xz
Source1531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcite.tar.xz
Source1532:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcite.doc.tar.xz
Source1664:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetexconfig.tar.xz
Source2108:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcharter.tar.xz
Source2109:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcharter.doc.tar.xz
Source2110:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xits.tar.xz
Source2111:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xits.doc.tar.xz
Source2113:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yfonts.tar.xz
Source2114:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yfonts.doc.tar.xz
Source2118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zlmtt.tar.xz
Source2119:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zlmtt.doc.tar.xz
Source2163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zapfchan.tar.xz
Source2164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zapfding.tar.xz
Source2258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xq.tar.xz
Source2259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xq.doc.tar.xz
Source2260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xskak.tar.xz
Source2261:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xskak.doc.tar.xz
Source2339:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xlop.tar.xz
Source2340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xlop.doc.tar.xz
Source2342:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yax.tar.xz
Source2343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yax.doc.tar.xz
Source2369:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xmltexconfig.tar.xz
Source2483:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xyling.tar.xz
Source2484:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xyling.doc.tar.xz
Source2509:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcjk2uni.tar.xz
Source2510:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcjk2uni.doc.tar.xz
Source2512:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zxjafont.tar.xz
Source2513:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zxjafont.doc.tar.xz
Source2525:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpinyin.tar.xz
Source2526:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpinyin.doc.tar.xz
Source2528:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhmetrics.tar.xz
Source2529:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhmetrics.doc.tar.xz
Source2531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhnumber.tar.xz
Source2532:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhnumber.doc.tar.xz
Source2534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhspacing.tar.xz
Source2535:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhspacing.doc.tar.xz
Source2665:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetexref.doc.tar.xz
Source2829:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xgreek.tar.xz
Source2830:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xgreek.doc.tar.xz
Source2832:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yannisgr.tar.xz
Source2833:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yannisgr.doc.tar.xz
Source2846:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-devanagari.tar.xz
Source2847:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-devanagari.doc.tar.xz
Source2914:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zxjafbfont.tar.xz
Source2915:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zxjafbfont.doc.tar.xz
Source2916:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zxjatype.tar.xz
Source2917:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zxjatype.doc.tar.xz
Source2984:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xypic-tut-pt.doc.tar.xz
Source3370:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xifthen.tar.xz
Source3371:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xifthen.doc.tar.xz
Source3386:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpicture.tar.xz
Source3387:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpicture.doc.tar.xz
Source3389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xypic.tar.xz
Source3390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xypic.doc.tar.xz
Source5690:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xargs.tar.xz
Source5691:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xargs.doc.tar.xz
Source5693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcolor-solarized.tar.xz
Source5694:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcolor-solarized.doc.tar.xz
Source5696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcomment.tar.xz
Source5697:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcomment.doc.tar.xz
Source5698:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xdoc.tar.xz
Source5699:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xdoc.doc.tar.xz
Source5701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xfor.tar.xz
Source5702:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xfor.doc.tar.xz
Source5704:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xhfill.tar.xz
Source5705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xhfill.doc.tar.xz
Source5706:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xint.tar.xz
Source5707:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xint.doc.tar.xz
Source5709:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xmpincl.tar.xz
Source5710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xmpincl.doc.tar.xz
Source5712:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xnewcommand.tar.xz
Source5713:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xnewcommand.doc.tar.xz
Source5714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xoptarg.tar.xz
Source5715:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xoptarg.doc.tar.xz
Source5716:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpatch.tar.xz
Source5717:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpatch.doc.tar.xz
Source5719:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpeek.tar.xz
Source5720:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpeek.doc.tar.xz
Source5722:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xprintlen.tar.xz
Source5723:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xprintlen.doc.tar.xz
Source5724:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpunctuate.tar.xz
Source5725:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpunctuate.doc.tar.xz
Source5727:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xstring.tar.xz
Source5728:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xstring.doc.tar.xz
Source5729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xtab.tar.xz
Source5730:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xtab.doc.tar.xz
Source5732:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xwatermark.tar.xz
Source5733:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xwatermark.doc.tar.xz
Source5734:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xytree.tar.xz
Source5735:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xytree.doc.tar.xz
Source5736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yafoot.tar.xz
Source5737:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yafoot.doc.tar.xz
Source5739:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yagusylo.tar.xz
Source5740:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yagusylo.doc.tar.xz
Source5742:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ydoc.tar.xz
Source5743:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ydoc.doc.tar.xz
Source5747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zed-csp.tar.xz
Source5748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zed-csp.doc.tar.xz
Source5749:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ziffer.tar.xz
Source5750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ziffer.doc.tar.xz
Source5751:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zwgetfdate.tar.xz
Source5752:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zwgetfdate.doc.tar.xz
Source5753:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zwpagelayout.tar.xz
Source5754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zwpagelayout.doc.tar.xz
Source5940:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yhmath.tar.xz
Source5941:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yhmath.doc.tar.xz
Source5943:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ytableau.tar.xz
Source5944:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ytableau.doc.tar.xz
Source6065:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpiano.tar.xz
Source6066:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xpiano.doc.tar.xz
Source6118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xii.doc.tar.xz
Source6625:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcookybooky.tar.xz
Source6626:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcookybooky.doc.tar.xz
Source6628:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yathesis.tar.xz
Source6629:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yathesis.doc.tar.xz
Source6631:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/york-thesis.tar.xz
Source6632:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/york-thesis.doc.tar.xz
Source6744:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xymtex.tar.xz
Source6745:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xymtex.doc.tar.xz
Source6747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/youngtab.tar.xz
Source6748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/youngtab.doc.tar.xz
Source6779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xebaposter.tar.xz
Source6780:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xebaposter.doc.tar.xz
Source6781:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xecjk.tar.xz
Source6782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xecjk.doc.tar.xz
Source6784:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xecolor.tar.xz
Source6785:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xecolor.doc.tar.xz
Source6786:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xecyr.tar.xz
Source6787:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xecyr.doc.tar.xz
Source6788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xeindex.tar.xz
Source6789:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xeindex.doc.tar.xz
Source6790:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xepersian.tar.xz
Source6791:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xepersian.doc.tar.xz
Source6793:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xesearch.tar.xz
Source6794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xesearch.doc.tar.xz
Source6795:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xespotcolor.tar.xz
Source6796:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xespotcolor.doc.tar.xz
Source6799:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-itrans.tar.xz
Source6800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-itrans.doc.tar.xz
Source6801:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-pstricks.tar.xz
Source6802:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-pstricks.doc.tar.xz
Source6803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-tibetan.tar.xz
Source6804:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex-tibetan.doc.tar.xz
Source6805:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetexfontinfo.tar.xz
Source6806:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetexfontinfo.doc.tar.xz
Source6807:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetexko.tar.xz
Source6808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetexko.doc.tar.xz
Source6809:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xevlna.tar.xz
Source6810:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xevlna.doc.tar.xz
Source6811:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xltxtra.tar.xz
Source6812:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xltxtra.doc.tar.xz
Source6814:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xunicode.tar.xz
Source6815:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xunicode.doc.tar.xz
Source7554:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xassoccnt.tar.xz
Source7555:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xassoccnt.doc.tar.xz
Source7556:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcntperchap.tar.xz
Source7557:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcntperchap.doc.tar.xz
Source7558:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xduthesis.tar.xz
Source7559:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xduthesis.doc.tar.xz
Source7561:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xellipsis.tar.xz
Source7562:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xellipsis.doc.tar.xz
Source7567:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xsavebox.tar.xz
Source7568:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xsavebox.doc.tar.xz
Source7570:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ycbook.tar.xz
Source7571:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ycbook.doc.tar.xz
Source7572:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yfonts-t1.tar.xz
Source7573:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yfonts-t1.doc.tar.xz
Source7574:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yinit-otf.tar.xz
Source7575:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yinit-otf.doc.tar.xz
Source7576:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhmetrics-uptex.tar.xz
Source7577:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhmetrics-uptex.doc.tar.xz
Source8016:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcolor-material.tar.xz
Source8017:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xcolor-material.doc.tar.xz
Source8018:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xechangebar.tar.xz
Source8019:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xechangebar.doc.tar.xz
Source8020:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xltabular.tar.xz
Source8021:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xltabular.doc.tar.xz
Source8022:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xsim.tar.xz
Source8023:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xsim.doc.tar.xz
Source8024:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yaletter.tar.xz
Source8025:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yaletter.doc.tar.xz
Source8026:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zebra-goodies.tar.xz
Source8027:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zebra-goodies.doc.tar.xz
Source8028:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhlipsum.tar.xz
Source8029:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/zhlipsum.doc.tar.xz
Source8050:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xii-lat.doc.tar.xz
Source8051:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xii-lat.tar.xz
Source8384:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xfakebold.tar.xz
Source8385:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xfakebold.doc.tar.xz
Source8388:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xtuthesis.tar.xz
Source8389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xtuthesis.doc.tar.xz
Source8390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xurl.tar.xz
Source8391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xurl.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-xcite
Provides:       tex-xcite = %{tl_version}
License:        LPPL 1.3
Summary:        Use citation keys from a different document
Version:        svn23783.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xcite.sty) = %{tl_version}

%description -n texlive-xcite
The package lets you use citation keys from another document,
just as the xr package allows cross-document use of labels.

%package -n texlive-xcite-doc
Summary:        Documentation for xcite
Version:        svn23783.1.0

Provides:       tex-xcite-doc
AutoReqProv:    No

%description -n texlive-xcite-doc
Documentation for xcite

%package -n texlive-xetex-devanagari
Provides:       tex-xetex-devanagari = %{tl_version}
License:        LPPL
Summary:        XeTeX input map for Unicode Devanagari
Version:        svn34296.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(devanagarinumerals.map) = %{tl_version}
Provides:       tex(harvardkyoto.map) = %{tl_version}, tex(iast.map) = %{tl_version}
Provides:       tex(velthuis-sanskrit.map) = %{tl_version}
Provides:       tex(velthuis.map) = %{tl_version}

%description -n texlive-xetex-devanagari
The package provides a map for use with Jonathan Kew's TECkit,
to translate Devanagari (encoded according to the Harvard/Kyoto
convention) to Unicode (range 0900-097F).

%package -n texlive-xetex-devanagari-doc
Summary:        Documentation for xetex-devanagari
Version:        svn34296.0.5

Provides:       tex-xetex-devanagari-doc
AutoReqProv:    No

%description -n texlive-xetex-devanagari-doc
Documentation for xetex-devanagari

%package -n texlive-xetexconfig
Provides:       tex-xetexconfig = %{tl_version}
License:        LPPL
Summary:        Configuration files for XeTeX
Version:        svn45845
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(crop.cfg) = %{tl_version}

%description -n texlive-xetexconfig
special crop.cfg for XeTeX

%package -n texlive-xcharter
Provides:       tex-xcharter = %{tl_version}
License:        MIT
Summary:        Extension of Bitstream Charter fonts
Version:        svn47941
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(mweights.sty), tex(etoolbox.sty), tex(fontaxes.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(chalph.enc) = %{tl_version}, tex(chtabosf.enc) = %{tl_version}
Provides:       tex(xch1_bwwzc2.enc) = %{tl_version}, tex(xch1_ch2jyx.enc) = %{tl_version}
Provides:       tex(xch1_d2abnl.enc) = %{tl_version}, tex(xch1_gq3a6i.enc) = %{tl_version}
Provides:       tex(xch1_jfcsri.enc) = %{tl_version}, tex(xch1_jltj6c.enc) = %{tl_version}
Provides:       tex(xch1_ks4pfu.enc) = %{tl_version}, tex(xch1_lq6vvn.enc) = %{tl_version}
Provides:       tex(xch1_sq3mdu.enc) = %{tl_version}, tex(xch1_w7s2xk.enc) = %{tl_version}
Provides:       tex(xch1_wy7dbt.enc) = %{tl_version}, tex(xch1_zcck2t.enc) = %{tl_version}
Provides:       tex(xch_2663q7.enc) = %{tl_version}, tex(xch_2b3ply.enc) = %{tl_version}
Provides:       tex(xch_aprite.enc) = %{tl_version}, tex(xch_atk3my.enc) = %{tl_version}
Provides:       tex(xch_bwwzc2.enc) = %{tl_version}, tex(xch_ch2jyx.enc) = %{tl_version}
Provides:       tex(xch_d2abnl.enc) = %{tl_version}, tex(xch_eofewb.enc) = %{tl_version}
Provides:       tex(xch_ft2zfi.enc) = %{tl_version}, tex(xch_gq3a6i.enc) = %{tl_version}
Provides:       tex(xch_h3miu6.enc) = %{tl_version}, tex(xch_hoftv6.enc) = %{tl_version}
Provides:       tex(xch_jfcsri.enc) = %{tl_version}, tex(xch_jltj6c.enc) = %{tl_version}
Provides:       tex(xch_kdlizx.enc) = %{tl_version}, tex(xch_ks4pfu.enc) = %{tl_version}
Provides:       tex(xch_lq6vvn.enc) = %{tl_version}, tex(xch_sq3mdu.enc) = %{tl_version}
Provides:       tex(xch_tdq2l3.enc) = %{tl_version}, tex(xch_tuu2ww.enc) = %{tl_version}
Provides:       tex(xch_uoltgb.enc) = %{tl_version}, tex(xch_w7s2xk.enc) = %{tl_version}
Provides:       tex(xch_wy7dbt.enc) = %{tl_version}, tex(xch_y6sx2d.enc) = %{tl_version}
Provides:       tex(xch_zcck2t.enc) = %{tl_version}, tex(XCharter.map) = %{tl_version}
Provides:       tex(XCharter-Bold.otf) = %{tl_version}, tex(XCharter-BoldItalic.otf) = %{tl_version}
Provides:       tex(XCharter-Italic.otf) = %{tl_version}
Provides:       tex(XCharter-Roman.otf) = %{tl_version}, tex(XCharter-Bol-osf.tfm) = %{tl_version}
Provides:       tex(XCharter-BolIta-alph.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-Ita-alph.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-sup-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-sup-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-sup-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter-osf.tfm) = %{tl_version}, tex(XCharter1-Bold-to.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-to.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-to.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-to.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-t1.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(zchbmi.tfm) = %{tl_version}, tex(zchmi.tfm) = %{tl_version}
Provides:       tex(XCharter-Bold.pfb) = %{tl_version}, tex(XCharter-BoldItalic.pfb) = %{tl_version}
Provides:       tex(XCharter-Italic.pfb) = %{tl_version}
Provides:       tex(XCharter-Roman.pfb) = %{tl_version}, tex(XCharter-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-sup-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-sup-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tlf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter-Roman-tosf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter1-Bold-to.vf) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-to.vf) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter1-Italic-to.vf) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(XCharter1-Roman-to.vf) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-t1.vf) = %{tl_version}
Provides:       tex(XCharter1-Roman-tosf-ts1.vf) = %{tl_version}
Provides:       tex(zchbmi.vf) = %{tl_version}, tex(zchmi.vf) = %{tl_version}
Provides:       tex(LY1XCharter-Sup.fd) = %{tl_version}, tex(LY1XCharter-TLF.fd) = %{tl_version}
Provides:       tex(LY1XCharter-TOsF.fd) = %{tl_version}
Provides:       tex(OT1XCharter-Sup.fd) = %{tl_version}, tex(OT1XCharter-TLF.fd) = %{tl_version}
Provides:       tex(OT1XCharter-TOsF.fd) = %{tl_version}
Provides:       tex(T1XCharter-Sup.fd) = %{tl_version}, tex(T1XCharter-TLF.fd) = %{tl_version}
Provides:       tex(T1XCharter-TOsF.fd) = %{tl_version}, tex(TS1XCharter-TLF.fd) = %{tl_version}
Provides:       tex(TS1XCharter-TOsF.fd) = %{tl_version}
Provides:       tex(XCharter.sty) = %{tl_version}, tex(omlzchmi.fd) = %{tl_version}

%description -n texlive-xcharter
The package presents an extension of Bitstream Charter, which
provides small caps, oldstyle figures and superior figures in
all four styles, accompanied by LaTeX font support files. The
fonts themselves are provided in both Adobe Type 1 and OTF
formats, with supporting files as necessary.

%package -n texlive-xcharter-doc
Summary:        Documentation for xcharter
Version:        svn47941
Provides:       tex-xcharter-doc
AutoReqProv:    No

%description -n texlive-xcharter-doc
Documentation for xcharter

%package -n texlive-xii-doc
Summary:        Documentation for xii
Version:        svn31683.0

Provides:       tex-xii-doc
AutoReqProv:    No

%description -n texlive-xii-doc
Documentation for xii

%package -n texlive-xii-lat
Summary:        Christmas silliness (Latin)
Version:        svn45805
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%description -n texlive-xii-lat
This is the plain TeX file xii-lat.tex. Call "pdftex
xii-lat.tex" to produce a (perhaps) surprising typeset
document.

%package -n texlive-xits
Provides:       tex-xits = %{tl_version}
License:        OFL
Summary:        A Scientific Times-like font with support for mathematical typesetting
Version:        svn32763.1.108

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xits-bold.otf) = %{tl_version}, tex(xits-bolditalic.otf) = %{tl_version}
Provides:       tex(xits-italic.otf) = %{tl_version}, tex(xits-math.otf) = %{tl_version}
Provides:       tex(xits-mathbold.otf) = %{tl_version}, tex(xits-regular.otf) = %{tl_version}

%description -n texlive-xits
XITS is a Times-like font for scientific typesetting with
proper mathematical support for modern, Unicode and OpenType
capable TeX engines, namely LuaTeX and XeTeX. For use with
LuaLaTeX or XeLaTeX, support is available from the fontspec and
unicode-math packages.

%package -n texlive-xits-doc
Summary:        Documentation for xits
Version:        svn32763.1.108

Provides:       tex-xits-doc
AutoReqProv:    No

%description -n texlive-xits-doc
Documentation for xits

%package -n texlive-yfonts
Provides:       tex-yfonts = %{tl_version}
License:        LPPL
Summary:        Support for old German fonts
Version:        svn15878.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(yfonts.sty) = %{tl_version}

%description -n texlive-yfonts
A LaTeX interface to the old-german fonts designed by Yannis
Haralambous: Gothic, Schwabacher, Fraktur and the baroque
initials.

%package -n texlive-yfonts-doc
Summary:        Documentation for yfonts
Version:        svn15878.1.3

Provides:       tex-yfonts-doc
AutoReqProv:    No

%description -n texlive-yfonts-doc
Documentation for yfonts

%package -n texlive-yfonts-t1
Provides:       tex-yfonts-t1 = %{tl_version}
License:        LPPL
Summary:        Old German-style fonts, in Adobe type 1 format
Version:        svn36013

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(yfrak.afm) = %{tl_version}, tex(ygoth.afm) = %{tl_version}
Provides:       tex(yswab.afm) = %{tl_version}, tex(yfrak.map) = %{tl_version}
Provides:       tex(yfrak.pfb) = %{tl_version}, tex(ygoth.pfb) = %{tl_version}
Provides:       tex(yswab.pfb) = %{tl_version}

%description -n texlive-yfonts-t1
This package comprises type 1 versions of the Gothic,
Schwabacher and Fraktur fonts of Yannis Haralambous' set of old
German fonts.

%package -n texlive-yfonts-t1-doc
Summary:        Documentation for yfonts-t1
Version:        svn36013

Provides:       tex-yfonts-t1-doc
AutoReqProv:    No

%description -n texlive-yfonts-t1-doc
Documentation for yfonts-t1.

%package -n texlive-yhmath
Provides:       tex-yhmath = %{tl_version}
License:        LPPL
Summary:        Extended maths fonts for LaTeX
Version:        svn46501
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(amsmath.sty)
Provides:       tex(yhmath.map) = %{tl_version}, tex(yhcmex10.tfm) = %{tl_version}
Provides:       tex(yrcmex10.tfm) = %{tl_version}, tex(yhcmex.pfb) = %{tl_version}
Provides:       tex(yhcmex10.vf) = %{tl_version}, tex(OMXyhex.fd) = %{tl_version}
Provides:       tex(yhmath.sty) = %{tl_version}

%description -n texlive-yhmath
The yhmath bundle contains fonts (in type 1 format) and a LaTeX
package for using them.

%package -n texlive-yhmath-doc
Summary:        Documentation for yhmath
Version:        svn46501
Provides:       tex-yhmath-doc
AutoReqProv:    No

%description -n texlive-yhmath-doc
Documentation for yhmath

%package -n texlive-ytableau
Provides:       tex-ytableau = %{tl_version}
License:        LPPL 1.2
Summary:        Many-featured Young tableaux and Young diagrams
Version:        svn27430.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgfkeys.sty), tex(pgfopts.sty), tex(xcolor.sty)
Provides:       tex(ytableau.sty) = %{tl_version}

%description -n texlive-ytableau
The package provides several functions for drawing Young
tableaux and Young diagrams, extending the young and youngtab
packages but providing lots more features. Skew and coloured
tableaux are easy, and pgfkeys-enabled options are provided
both at package load and configurably.

%package -n texlive-ytableau-doc
Summary:        Documentation for ytableau
Version:        svn27430.1.3

Provides:       tex-ytableau-doc
AutoReqProv:    No

%description -n texlive-ytableau-doc
Documentation for ytableau

%package -n texlive-zlmtt
Provides:       tex-zlmtt = %{tl_version}
License:        LPPL 1.3
Summary:        Use Latin Modern Typewriter fonts
Version:        svn34485.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(mweights.sty), tex(xkeyval.sty)
Provides:       tex(il2zlmtt.fd) = %{tl_version}, tex(il2zlmvtt.fd) = %{tl_version}
Provides:       tex(l7xzlmtt.fd) = %{tl_version}, tex(l7xzlmvtt.fd) = %{tl_version}
Provides:       tex(ly1zlmtt.fd) = %{tl_version}, tex(ly1zlmvtt.fd) = %{tl_version}
Provides:       tex(ot1zlmtt.fd) = %{tl_version}, tex(ot1zlmvtt.fd) = %{tl_version}
Provides:       tex(ot4zlmtt.fd) = %{tl_version}, tex(ot4zlmvtt.fd) = %{tl_version}
Provides:       tex(qxzlmtt.fd) = %{tl_version}, tex(qxzlmvtt.fd) = %{tl_version}
Provides:       tex(t1zlmtt.fd) = %{tl_version}, tex(t1zlmvtt.fd) = %{tl_version}
Provides:       tex(t5zlmtt.fd) = %{tl_version}, tex(t5zlmvtt.fd) = %{tl_version}
Provides:       tex(ts1zlmtt.fd) = %{tl_version}, tex(ts1zlmvtt.fd) = %{tl_version}
Provides:       tex(zlmtt.sty) = %{tl_version}

%description -n texlive-zlmtt
The package allows selection of Latin Modern Typewriter fonts
with scaling and access to all its features. The package
requires the mweights package.

%package -n texlive-zlmtt-doc
Summary:        Documentation for zlmtt
Version:        svn34485.1.01

Provides:       tex-zlmtt-doc
AutoReqProv:    No

%description -n texlive-zlmtt-doc
Documentation for zlmtt

%package -n texlive-zapfchan
Provides:       tex-zapfchan = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(uzc.map) = %{tl_version}, tex(pzcmi.tfm) = %{tl_version}
Provides:       tex(pzcmi7t.tfm) = %{tl_version}, tex(pzcmi8c.tfm) = %{tl_version}
Provides:       tex(pzcmi8r.tfm) = %{tl_version}, tex(pzcmi8t.tfm) = %{tl_version}
Provides:       tex(uzcmi7t.tfm) = %{tl_version}, tex(uzcmi8c.tfm) = %{tl_version}
Provides:       tex(uzcmi8r.tfm) = %{tl_version}, tex(uzcmi8t.tfm) = %{tl_version}
Provides:       tex(uzcmi8a.pfb) = %{tl_version}, tex(pzcmi.vf) = %{tl_version}
Provides:       tex(pzcmi7t.vf) = %{tl_version}, tex(pzcmi8c.vf) = %{tl_version}
Provides:       tex(pzcmi8t.vf) = %{tl_version}, tex(uzcmi7t.vf) = %{tl_version}
Provides:       tex(uzcmi8c.vf) = %{tl_version}, tex(uzcmi8t.vf) = %{tl_version}
Provides:       tex(8ruzc.fd) = %{tl_version}, tex(omluzc.fd) = %{tl_version}
Provides:       tex(omsuzc.fd) = %{tl_version}, tex(ot1uzc.fd) = %{tl_version}
Provides:       tex(t1uzc.fd) = %{tl_version}, tex(ts1uzc.fd) = %{tl_version}

%description -n texlive-zapfchan
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-zapfding
Provides:       tex-zapfding = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(uzd.map) = %{tl_version}, tex(pzdr.tfm) = %{tl_version}
Provides:       tex(uzdr.tfm) = %{tl_version}, tex(uzdr.pfb) = %{tl_version}
Provides:       tex(uuzd.fd) = %{tl_version}

%description -n texlive-zapfding
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-xq
Provides:       tex-xq = %{tl_version}
License:        LPPL
Summary:        Support for writing about xiangqi
Version:        svn35211.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xqlarge.tfm) = %{tl_version}, tex(xqnormal.tfm) = %{tl_version}
Provides:       tex(xq.sty) = %{tl_version}

%description -n texlive-xq
The package is for writing about xiangqi or chinese chess. You
can write games or parts of games and show diagrams with
special positions.

%package -n texlive-xq-doc
Summary:        Documentation for xq
Version:        svn35211.0.4

Provides:       tex-xq-doc
AutoReqProv:    No

%description -n texlive-xq-doc
Documentation for xq

%package -n texlive-xskak
Provides:       tex-xskak = %{tl_version}
License:        LPPL
Summary:        An extension to the skak package for chess typesetting
Version:        svn35945.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xifthen.sty), tex(etoolbox.sty), tex(chessboard.sty)
Provides:       tex(xskak-keys.sty) = %{tl_version}, tex(xskak-nagdef.sty) = %{tl_version}
Provides:       tex(xskak.sty) = %{tl_version}

%description -n texlive-xskak
Xskak, as its prime function, saves information about a chess
game for later use (e.g., to loop through a game to make an
animated board). The package also extends the input that the
parsing commands can handle and offers an interface to define
and switch between indefinite levels of styles.

%package -n texlive-xskak-doc
Summary:        Documentation for xskak
Version:        svn35945.1.4

Provides:       tex-xskak-doc
AutoReqProv:    No

%description -n texlive-xskak-doc
Documentation for xskak

%package -n texlive-xlop
Provides:       tex-xlop = %{tl_version}
License:        LPPL
Summary:        Calculates and displays arithmetic operations
Version:        svn42899
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(xlop.sty) = %{tl_version}, tex(xlop.tex) = %{tl_version}

%description -n texlive-xlop
Xlop (eXtra Large OPeration) will typeset arithmetic problems
either in-line or "as in school" (using French school
conventions). So for example, \opadd{2}{3} can give either
$2+3=5$ or something similar to: \begin{tabular}{r} 2\\ +3\\
\hline 5\end{tabular}. Furthermore, numbers may be very large,
e.g 200 figures (with a very long compilation time). Many other
features allow to deal with numbers (tests, display, some high
level operations, etc.)

%package -n texlive-xlop-doc
Summary:        Documentation for xlop
Version:        svn42899
Provides:       tex-xlop-doc
AutoReqProv:    No

%description -n texlive-xlop-doc
Documentation for xlop

%package -n texlive-yax
Provides:       tex-yax = %{tl_version}
License:        LPPL
Summary:        Yet Another Key System
Version:        svn21183.1.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(t-yax.tex) = %{tl_version}, tex(yax.sty) = %{tl_version}
Provides:       tex(yax.tex) = %{tl_version}

%description -n texlive-yax
YaX is advertised as a key system, but it rather organizes
attributes in parameters, which parameters can be executed, so
that YaX is halfway between key management and macro definition
(and actually hopes to provide a user's interface). Values
assigned to attributes can be retrieved and tested in various
ways, with full expandability ensured as much as possible.
Finally, YaX's syntax is a quite peculiar (as few braces as
possible), but may be customized. YaX is based on texapi and
thus requires e-TeX.

%package -n texlive-yax-doc
Summary:        Documentation for yax
Version:        svn21183.1.03

Provides:       tex-yax-doc
AutoReqProv:    No

%description -n texlive-yax-doc
Documentation for yax

%package -n texlive-xargs
Provides:       tex-xargs = %{tl_version}
License:        LPPL
Summary:        Define commands with many optional arguments
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty)
Provides:       tex(xargs.sty) = %{tl_version}

%description -n texlive-xargs
The package provides extended versions of \newcommand and
related LaTeX commands, which allow easy and robust definition
of macros with many optional arguments, using a clear and
simple xkeyval-style syntax.

%package -n texlive-xargs-doc
Summary:        Documentation for xargs
Version:        svn15878.1.1

Provides:       tex-xargs-doc
AutoReqProv:    No

%description -n texlive-xargs-doc
Documentation for xargs

%package -n texlive-xkeyval
Provides:       tex-xkeyval = %{tl_version}
License:        LPPL 1.3
Summary:        Extension of the keyval package
Version:        svn35741.2.7a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(longtable.sty)
Provides:       tex(keyval.tex) = %{tl_version}, tex(pst-xkey.tex) = %{tl_version}
Provides:       tex(xkeyval.tex) = %{tl_version}, tex(xkvex1.tex) = %{tl_version}
Provides:       tex(xkvex2.tex) = %{tl_version}, tex(xkvex3.tex) = %{tl_version}
Provides:       tex(xkvex4.tex) = %{tl_version}, tex(xkvtxhdr.tex) = %{tl_version}
Provides:       tex(xkvutils.tex) = %{tl_version}, tex(pst-xkey.sty) = %{tl_version}
Provides:       tex(xkeyval.sty) = %{tl_version}, tex(xkveca.cls) = %{tl_version}
Provides:       tex(xkvecb.cls) = %{tl_version}, tex(xkvesa.sty) = %{tl_version}
Provides:       tex(xkvesb.sty) = %{tl_version}, tex(xkvesc.sty) = %{tl_version}
Provides:       tex(xkvltxp.sty) = %{tl_version}, tex(xkvview.sty) = %{tl_version}

%description -n texlive-xkeyval
This package is an extension of the keyval package and offers
additional macros for setting keys and declaring and setting
class or package options. The package allows the programmer to
specify a prefix to the name of the macros it defines for keys,
and to define families of key definitions; these all help use
in documents where several packages define their own sets of
keys.

%package -n texlive-xkeyval-doc
Summary:        Documentation for xkeyval
Version:        svn35741.2.7a

Provides:       tex-xkeyval-doc
AutoReqProv:    No

%description -n texlive-xkeyval-doc
Documentation for xkeyval

%package -n texlive-xcolor
Provides:       tex-xcolor = %{tl_version}
License:        LPPL
Summary:        Driver-independent color extensions for LaTeX and pdfLaTeX
Version:        svn41044

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-graphics-cfg, tex(colortbl.sty), tex(pdfcolmk.sty)
Provides:       tex(svgnam.def) = %{tl_version}, tex(x11nam.def) = %{tl_version}
Provides:       tex(xcolor.sty) = %{tl_version}

%description -n texlive-xcolor
The package starts from the basic facilities of the color
package, and provides easy driver-independent access to several
kinds of color tints, shades, tones, and mixes of arbitrary
colors. It allows a user to select a document-wide target color
model and offers complete tools for conversion between eight
color models. Additionally, there is a command for alternating
row colors plus repeated non-aligned material (like horizontal
lines) in tables. Colors can be mixed like
\color{red!30!green!40!blue}.

%package -n texlive-xcolor-doc
Summary:        Documentation for xcolor
Version:        svn41044

Provides:       tex-xcolor-doc
AutoReqProv:    No

%description -n texlive-xcolor-doc
Documentation for xcolor

%package -n texlive-xcolor-solarized
Provides:       tex-xcolor-solarized = %{tl_version}
License:        LPPL 1.3
Summary:        Defines the 16 colors from Ethan Schoonover's Solarized palette
Version:        svn41809
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xcolor.sty), tex(kvoptions.sty)
Provides:       tex(xcolor-solarized.sty) = %{tl_version}

%description -n texlive-xcolor-solarized
Built on top of the package, this package defines the sixteen
colors of Ethan Schoonover's popular color palette, Solarized,
for use in documents typeset with LaTeX and Friends.

%package -n texlive-xcolor-solarized-doc
Summary:        Documentation for xcolor-solarized
Version:        svn41809
Provides:       tex-xcolor-solarized-doc
AutoReqProv:    No

%description -n texlive-xcolor-solarized-doc
Documentation for xcolor-solarized

%package -n texlive-xcolor-material
Summary:        Defines the 256 colors from Google Material Color Palette
Version:        svn42289
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(xcolor-material.sty) = %{tl_version}

%description -n texlive-xcolor-material
The package is built on top of the great xcolor package. It
provides a useful definition of the beautiful Google Material
Color Palette, available at Google Material design, for its use
in document writing with LaTeX and Friends.

%package -n texlive-xechangebar
Summary:        An extension of package changebar that can be used with XeLaTeX
Version:        svn44954
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(xechangebar.sty) = %{tl_version}

%description -n texlive-xechangebar
The package extends package changebar so it can be used with
XeLaTeX. It introduces the new option xetex for use with
XeLaTeX. Everything else remains the same and users should
consult the original documenation for usage information.

%package -n texlive-xltabular
Summary:        Longtable support with possible X-column specifier
Version:        svn47829
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(xltabular.sty) = %{tl_version}

%description -n texlive-xltabular
This package loads package ltablex, but keeps the current
tabularx environment as is. The new environment xltabular is a
combination of longtable and tabularx: Header/footer
definitions, X-column specifier, and with possible pagebreaks.

%package -n texlive-xsim
Summary:        eXercise Sheets IMproved
Version:        svn46634
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(xsim-manual.cls) = %{tl_version}, tex(xsim.auxfile.code.tex) = %{tl_version}
Provides:       tex(xsim.base.code.tex) = %{tl_version}, tex(xsim.blanks.code.tex) = %{tl_version}
Provides:       tex(xsim.collections.code.tex) = %{tl_version}
Provides:       tex(xsim.definitions.code.tex) = %{tl_version}
Provides:       tex(xsim.environments.code.tex) = %{tl_version}
Provides:       tex(xsim.exercises.code.tex) = %{tl_version}
Provides:       tex(xsim.goals.code.tex) = %{tl_version}
Provides:       tex(xsim.grades.code.tex) = %{tl_version}
Provides:       tex(xsim.interface.code.tex) = %{tl_version}
Provides:       tex(xsim.layouts.code.tex) = %{tl_version}
Provides:       tex(xsim.modules.code.tex) = %{tl_version}
Provides:       tex(xsim.properties.code.tex) = %{tl_version}
Provides:       tex(xsim.random.code.tex) = %{tl_version}
Provides:       tex(xsim.solutions.code.tex) = %{tl_version}
Provides:       tex(xsim.sty) = %{tl_version}, tex(xsim.tags.code.tex) = %{tl_version}
Provides:       tex(xsim.templates.code.tex) = %{tl_version}
Provides:       tex(xsim.translations.code.tex) = %{tl_version}
Provides:       tex(xsim.verbwrite.code.tex) = %{tl_version}
Provides:       tex(xsimverb.sty) = %{tl_version}

%description -n texlive-xsim
This package helps in creating exercises and the corresponding
solutions. It is the official successor of the exsheets package
and fixes/improves various long-standing issues.

%package -n texlive-yaletter
Summary:        Extremely flexible macros for letters, envelopes, and label sheets
Version:        svn42830
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(yaletter.cls) = %{tl_version}

%description -n texlive-yaletter
The yaletter class provides extremely configurable macros for
typesetting letters in any conceivable style. It provides
facilities for maintaining easily-accessible databases of
letterheads and addresses for repeat use. It further provides
easy macros for envelopes and for label sheets. Finally, it
provides some nice defaults for a few of the more common styles
and sizes.

%package -n texlive-zebra-goodies
Summary:        A collection of handy macros for paper writing
Version:        svn46004
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(zebra-goodies.sty) = %{tl_version}

%description -n texlive-zebra-goodies
This package offers a collection of macros to help in the
process of writing a paper. You may add comments, todo notes,
etc. during revision, in a colourful way. The package also
summarizes the inserted notes at the end of the document. There
are some predefined note commands as well as a way of defining
new ones to suit the user's needs. You may safely remove this
package once the paper is finished. This package depends on the
following other LaTeX packages: kvoptions, manfnt, marginnote,
tikzpagenodes, xcolor, and, optionally, microtype. Note:
"zebra" is the name of the package author's lab.

%package -n texlive-zhlipsum
Summary:        Chinese dummy text
Version:        svn47383
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(zhlipsum-zh-cn-gbk.def) = %{tl_version}
Provides:       tex(zhlipsum-zh-cn-utf8.def) = %{tl_version}
Provides:       tex(zhlipsum.sty) = %{tl_version}

%description -n texlive-zhlipsum
The package provides an interface to dummy text in Chinese,
which will be useful for testing Chinese documents. At present,
UTF-8 and GBK encodings are supported.

%package -n texlive-xcomment
Provides:       tex-xcomment = %{tl_version}
License:        LPPL
Summary:        Allows selected environments to be included/excluded
Version:        svn20031.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xcomment.sty) = %{tl_version}, tex(xcomment.tex) = %{tl_version}

%description -n texlive-xcomment
The package defines an environment that only typesets specified
environments within its scope. So, for example, if you want
nothing but the figure and table environments in your document,
you can enclose the whole document with an xcomment environment
that excludes everything but. This is a lot easier than
excluding the chunks of text between the environments you want,
or creating an entire document containing only those
environments. The package was previously part of the seminar
bundle for typesetting presentations.

%package -n texlive-xcomment-doc
Summary:        Documentation for xcomment
Version:        svn20031.1.3

Provides:       tex-xcomment-doc
AutoReqProv:    No

%description -n texlive-xcomment-doc
Documentation for xcomment

%package -n texlive-xdoc
Provides:       tex-xdoc = %{tl_version}
License:        LPPL
Summary:        Extending the LaTeX doc system
Version:        svn15878.prot2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(multicol.sty), tex(doc.sty)
Provides:       tex(docidx2e.sty) = %{tl_version}, tex(docindex.sty) = %{tl_version}
Provides:       tex(xdoc2.sty) = %{tl_version}

%description -n texlive-xdoc
Xdoc is a project to rewrite the implementation of the LaTeX
doc package (in a broader sense) to make its features more
general and flexible. For example, where doc only provides
commands for documenting macros and environments, xdoc also
provides commands for similarly documenting package options and
switches. This is furthermore done in such a way that it is
very easy to add more such commands for documenting things,
such as e.g., templates (an important concept in the future
LaTeX3) and program components for other languages (functions,
classes, procedures, etc.). A side effect is that many minor
bugs in doc are fixed. The design aims to take advantage of
many still experimental features of future versions of LaTeX,
but since these are neither reasonably stable nor widely
available, the configuration interfaces and package author
commands of xdoc are likely to change. To still provide a
stable interface for other packages to build upon, the actual
package names include a "major version number" of sorts. The
drop-in replacement package for standard doc is xdoc2; it
requires nothing outside standard LaTeX2e. The
docindex/docidx2e package changes the index and list of changes
typesetting so that none of the formatting has to be controlled
via the index style file. The docindex package provides control
of formatting via templates (nice interface, but requires
several experimental packages), whereas the docidx2e package
has traditional raw macro interfaces and works with standard
LaTeX2e.

%package -n texlive-xdoc-doc
Summary:        Documentation for xdoc
Version:        svn15878.prot2.5

Provides:       tex-xdoc-doc
AutoReqProv:    No

%description -n texlive-xdoc-doc
Documentation for xdoc

%package -n texlive-xfor
Provides:       tex-xfor = %{tl_version}
License:        LPPL
Summary:        A reimplementation of the LaTeX for-loop macro
Version:        svn15878.1.05

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xfor.sty) = %{tl_version}

%description -n texlive-xfor
The package redefines the LaTeX internal \@for macro so that
the loop may be prematurely terminated. The action is akin to
the C/Java break statement, except that the loop does not
terminate until the end of the current iteration

%package -n texlive-xfor-doc
Summary:        Documentation for xfor
Version:        svn15878.1.05

Provides:       tex-xfor-doc
AutoReqProv:    No

%description -n texlive-xfor-doc
Documentation for xfor

%package -n texlive-xhfill
Provides:       tex-xhfill = %{tl_version}
License:        LPPL
Summary:        Extending \hrulefill
Version:        svn22575.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(calc.sty), tex(xspace.sty)
Provides:       tex(xhfill.sty) = %{tl_version}

%description -n texlive-xhfill
The package provides extended macros for the default \hrulefill
command. It allows modification of the width and the colour of
the line.

%package -n texlive-xhfill-doc
Summary:        Documentation for xhfill
Version:        svn22575.1.01

Provides:       tex-xhfill-doc
AutoReqProv:    No

%description -n texlive-xhfill-doc
Documentation for xhfill

%package -n texlive-xifthen
Provides:       tex-xifthen = %{tl_version}
License:        LPPL
Summary:        Extended conditional commands
Version:        svn38929

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(calc.sty), tex(ifthen.sty), tex(ifmtarg.sty)
Provides:       tex(xifthen.sty) = %{tl_version}

%description -n texlive-xifthen
This package extends the ifthen package by implementing new
commands to go within the first argument of \ifthenelse: to
test whether a string is void or not, if a command is defined
or equivalent to another. The package also enables use of
complex expressions as introduced by the package calc, together
with the ability of defining new commands to handle complex
tests. The package requires e-TeX features.

%package -n texlive-xifthen-doc
Summary:        Documentation for xifthen
Version:        svn38929

Provides:       tex-xifthen-doc
AutoReqProv:    No

%description -n texlive-xifthen-doc
Documentation for xifthen

%package -n texlive-xint
Provides:       tex-xint = %{tl_version}
License:        LPPL 1.3
Summary:        Expandable operations on long numbers
Version:        svn48040
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xintfrac.sty), tex(xinttools.sty)
Provides:       tex(xint.sty) = %{tl_version}, tex(xintbinhex.sty) = %{tl_version}
Provides:       tex(xintcfrac.sty) = %{tl_version}, tex(xintcore.sty) = %{tl_version}
Provides:       tex(xintexpr.sty) = %{tl_version}, tex(xintfrac.sty) = %{tl_version}
Provides:       tex(xintgcd.sty) = %{tl_version}, tex(xintkernel.sty) = %{tl_version}
Provides:       tex(xintseries.sty) = %{tl_version}, tex(xinttools.sty) = %{tl_version}

%description -n texlive-xint
The bundle provides nine packages: xintcore, which provides
expandable TeX macros that implement the basic arithmetic
operations of addition, subtraction, multiplication and
division, as applied to arbitrarily long numbers represented as
chains of digits with an optional minus sign; xint, which
extends xintcore with more big integer operations; xinttools,
which provides utilities of independent interest such as
expandable and non-expandable loops; xintfrac, which computes
fractions using xint; xintexpr, which extends xintfrac with an
expandable parser of comma separated expressions involving
integers, fractions, boolean, and algebraic operators, and
declared as well as dummy variables; xintbinhex provides
conversions to and from binary and hexadecimal bases;
xintseries, which provides basic functionality for computing
partial sums using xint; xintgcd, which provides
implementations of the Euclidean algorithm, and of its
typesetting; xintcfrac, which deals with the computation of
continued fractions. All of the packages' computations are done
in a way that they can operate in an expanding environment. The
packages may be used either with Plain TeX or LaTeX.

%package -n texlive-xint-doc
Summary:        Documentation for xint
Version:        svn48040
Provides:       tex-xint-doc
AutoReqProv:    No

%description -n texlive-xint-doc
Documentation for xint

%package -n texlive-xmltexconfig
Provides:       tex-xmltexconfig = %{tl_version}
License:        LPPL
Summary:        xmltexconfig package
Version:        svn45845
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-xmltexconfig
xmltexconfig package

%package -n texlive-xmpincl
Provides:       tex-xmpincl = %{tl_version}
License:        GPL+
Summary:        Include eXtensible Metadata Platform data in PDFLaTeX
Version:        svn15878.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(ifthen.sty)
Provides:       tex(xmpincl.sty) = %{tl_version}

%description -n texlive-xmpincl
The XMP (eXtensible Metadata platform) is a framework to add
metadata to digital material to enhance the workflow in
publication. The essence is that the metadata is stored in an
XML file, and this XML stream is then embedded in the file to
which it applies. How you create this XML file is up to you,
but the author started investigating this because he wanted to
embed licensing information in the files he created. The
license the author chose is one of the Creative Commons
licenses, and their web-site offers this information in a valid
XML-file, suitable for direct inclusion.

%package -n texlive-xmpincl-doc
Summary:        Documentation for xmpincl
Version:        svn15878.2.2

Provides:       tex-xmpincl-doc
AutoReqProv:    No

%description -n texlive-xmpincl-doc
Documentation for xmpincl

%package -n texlive-xnewcommand
Provides:       tex-xnewcommand = %{tl_version}
License:        LPPL
Summary:        Define \global and \protected commands with \newcommand
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xnewcommand.sty) = %{tl_version}

%description -n texlive-xnewcommand
The package provides the means of defining \global and (e-TeX)
\protected commands, within the framework of LaTeX's standard
\newcommand.

%package -n texlive-xnewcommand-doc
Summary:        Documentation for xnewcommand
Version:        svn15878.1.2

Provides:       tex-xnewcommand-doc
AutoReqProv:    No

%description -n texlive-xnewcommand-doc
Documentation for xnewcommand

%package -n texlive-xoptarg
Provides:       tex-xoptarg = %{tl_version}
License:        LPPL
Summary:        Expandable macros that take an optional argument
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xoptarg.sty) = %{tl_version}

%description -n texlive-xoptarg
Commands that take an optional argument are not ordinarily
expandable; this package allows such commands to be expandable
provided that they have at least one mandatory argument.

%package -n texlive-xoptarg-doc
Summary:        Documentation for xoptarg
Version:        svn15878.1.0

Provides:       tex-xoptarg-doc
AutoReqProv:    No

%description -n texlive-xoptarg-doc
Documentation for xoptarg

%package -n texlive-xpatch
Provides:       tex-xpatch = %{tl_version}
License:        LPPL 1.3
Summary:        Extending etoolbox patching commands
Version:        svn27897.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(etoolbox.sty)
Provides:       tex(xpatch.sty) = %{tl_version}

%description -n texlive-xpatch
The package generalises the macro patching commands provided by
Philipp Lehmann's etoolbox.

%package -n texlive-xpatch-doc
Summary:        Documentation for xpatch
Version:        svn27897.0.2

Provides:       tex-xpatch-doc
AutoReqProv:    No

%description -n texlive-xpatch-doc
Documentation for xpatch

%package -n texlive-xpeek
Provides:       tex-xpeek = %{tl_version}
License:        LPPL 1.3
Summary:        Define commands that peek ahead in the input stream
Version:        svn27442.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(xpeek.sty) = %{tl_version}

%description -n texlive-xpeek
The package provides tools to help define commands that, like
\xspace and the LaTeX command \textit, peek at what follows
them in the command stream and choose appropriate behaviour.

%package -n texlive-xpeek-doc
Summary:        Documentation for xpeek
Version:        svn27442.0.2

Provides:       tex-xpeek-doc
AutoReqProv:    No

%description -n texlive-xpeek-doc
Documentation for xpeek

%package -n texlive-xpicture
Provides:       tex-xpicture = %{tl_version}
License:        LPPL 1.3
Summary:        Extensions of LaTeX picture drawing
Version:        svn28770.1.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(curve2e.sty), tex(xcolor.sty), tex(calculus.sty)
Provides:       tex(xpicture.sty) = %{tl_version}

%description -n texlive-xpicture
The package extends the facilities of the pict2e and the
curve2e packages, providing extra reference frames, conic
section curves, graphs of elementary functions and other
parametric curves.

%package -n texlive-xpicture-doc
Summary:        Documentation for xpicture
Version:        svn28770.1.2a

Provides:       tex-xpicture-doc
AutoReqProv:    No

%description -n texlive-xpicture-doc
Documentation for xpicture

%package -n texlive-xypic
Provides:       tex-xypic = %{tl_version}
License:        GPL+
Summary:        Flexible diagramming macros
Version:        svn31859.3.8.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty), tex(ifpdf.sty)
Provides:       tex(xycirc.enc) = %{tl_version}, tex(xyd.enc) = %{tl_version}
Provides:       tex(xyd2.enc) = %{tl_version}, tex(xypic.map) = %{tl_version}
Provides:       tex(xyatip10.tfm) = %{tl_version}, tex(xybsql10.tfm) = %{tl_version}
Provides:       tex(xybtip10.tfm) = %{tl_version}, tex(xycirc10.tfm) = %{tl_version}
Provides:       tex(xycmat10.tfm) = %{tl_version}, tex(xycmat11.tfm) = %{tl_version}
Provides:       tex(xycmat12.tfm) = %{tl_version}, tex(xycmbt10.tfm) = %{tl_version}
Provides:       tex(xycmbt11.tfm) = %{tl_version}, tex(xycmbt12.tfm) = %{tl_version}
Provides:       tex(xydash10.tfm) = %{tl_version}, tex(xyeuat10.tfm) = %{tl_version}
Provides:       tex(xyeuat11.tfm) = %{tl_version}, tex(xyeuat12.tfm) = %{tl_version}
Provides:       tex(xyeubt10.tfm) = %{tl_version}, tex(xyeubt11.tfm) = %{tl_version}
Provides:       tex(xyeubt12.tfm) = %{tl_version}, tex(xyline10.tfm) = %{tl_version}
Provides:       tex(xyluat10.tfm) = %{tl_version}, tex(xyluat11.tfm) = %{tl_version}
Provides:       tex(xyluat12.tfm) = %{tl_version}, tex(xylubt10.tfm) = %{tl_version}
Provides:       tex(xylubt11.tfm) = %{tl_version}, tex(xylubt12.tfm) = %{tl_version}
Provides:       tex(xymisc10.tfm) = %{tl_version}, tex(xyqc10.tfm) = %{tl_version}
Provides:       tex(xyatip10.pfb) = %{tl_version}, tex(xybsql10.pfb) = %{tl_version}
Provides:       tex(xybtip10.pfb) = %{tl_version}, tex(xycirc10.pfb) = %{tl_version}
Provides:       tex(xycmat10.pfb) = %{tl_version}, tex(xycmat11.pfb) = %{tl_version}
Provides:       tex(xycmat12.pfb) = %{tl_version}, tex(xycmbt10.pfb) = %{tl_version}
Provides:       tex(xycmbt11.pfb) = %{tl_version}, tex(xycmbt12.pfb) = %{tl_version}
Provides:       tex(xydash10.pfb) = %{tl_version}, tex(xyeuat10.pfb) = %{tl_version}
Provides:       tex(xyeuat11.pfb) = %{tl_version}, tex(xyeuat12.pfb) = %{tl_version}
Provides:       tex(xyeubt10.pfb) = %{tl_version}, tex(xyeubt11.pfb) = %{tl_version}
Provides:       tex(xyeubt12.pfb) = %{tl_version}, tex(xyluat10.pfb) = %{tl_version}
Provides:       tex(xyluat11.pfb) = %{tl_version}, tex(xyluat12.pfb) = %{tl_version}
Provides:       tex(xylubt10.pfb) = %{tl_version}, tex(xylubt11.pfb) = %{tl_version}
Provides:       tex(xylubt12.pfb) = %{tl_version}, tex(movie.cls) = %{tl_version}
Provides:       tex(xy.sty) = %{tl_version}, tex(xy.tex) = %{tl_version}
Provides:       tex(xy16textures.tex) = %{tl_version}, tex(xy17oztex.tex) = %{tl_version}
Provides:       tex(xy2cell.tex) = %{tl_version}, tex(xyall.tex) = %{tl_version}
Provides:       tex(xyarc.tex) = %{tl_version}, tex(xyarrow.tex) = %{tl_version}
Provides:       tex(xybarr.tex) = %{tl_version}, tex(xycmactex.tex) = %{tl_version}
Provides:       tex(xycmtip.tex) = %{tl_version}, tex(xycolor.tex) = %{tl_version}
Provides:       tex(xycrayon.tex) = %{tl_version}, tex(xycurve.tex) = %{tl_version}
Provides:       tex(xydummy.tex) = %{tl_version}, tex(xydvidrv.tex) = %{tl_version}
Provides:       tex(xydvips.tex) = %{tl_version}, tex(xydvitops.tex) = %{tl_version}
Provides:       tex(xyemtex.tex) = %{tl_version}, tex(xyframe.tex) = %{tl_version}
Provides:       tex(xygraph.tex) = %{tl_version}, tex(xyidioms.tex) = %{tl_version}
Provides:       tex(xyimport.tex) = %{tl_version}, tex(xyknot.tex) = %{tl_version}
Provides:       tex(xyline.tex) = %{tl_version}, tex(xymatrix.tex) = %{tl_version}
Provides:       tex(xymovie.tex) = %{tl_version}, tex(xynecula.tex) = %{tl_version}
Provides:       tex(xyoztex.tex) = %{tl_version}, tex(xypdf-co.tex) = %{tl_version}
Provides:       tex(xypdf-cu.tex) = %{tl_version}, tex(xypdf-fr.tex) = %{tl_version}
Provides:       tex(xypdf-li.tex) = %{tl_version}, tex(xypdf-ro.tex) = %{tl_version}
Provides:       tex(xypdf.tex) = %{tl_version}, tex(xypic.sty) = %{tl_version}
Provides:       tex(xypic.tex) = %{tl_version}, tex(xypicture.tex) = %{tl_version}
Provides:       tex(xypoly.tex) = %{tl_version}, tex(xyps-c.tex) = %{tl_version}
Provides:       tex(xyps-col.tex) = %{tl_version}, tex(xyps-f.tex) = %{tl_version}
Provides:       tex(xyps-l.tex) = %{tl_version}, tex(xyps-pro.tex) = %{tl_version}
Provides:       tex(xyps-ps.tex) = %{tl_version}, tex(xyps-r.tex) = %{tl_version}
Provides:       tex(xyps-s.tex) = %{tl_version}, tex(xyps-t.tex) = %{tl_version}
Provides:       tex(xyps.tex) = %{tl_version}, tex(xypsdict.tex) = %{tl_version}
Provides:       tex(xypspatt.tex) = %{tl_version}, tex(xyrecat.tex) = %{tl_version}
Provides:       tex(xyrotate.tex) = %{tl_version}, tex(xysmart.tex) = %{tl_version}
Provides:       tex(xytextures.tex) = %{tl_version}, tex(xytile.tex) = %{tl_version}
Provides:       tex(xytips.tex) = %{tl_version}, tex(xytp-f.tex) = %{tl_version}
Provides:       tex(xytpic.tex) = %{tl_version}, tex(xyv2.tex) = %{tl_version}
Provides:       tex(xyweb.tex) = %{tl_version}, tex(xyxdvi.tex) = %{tl_version}

%description -n texlive-xypic
A package for typesetting a variety of graphs and diagrams with
TeX. Xy-pic works with most formats (including LaTeX, AMS-
LaTeX, AMS-TeX, and plain TeX). The distribution includes
Michael Barr's diag package, which was previously distributed
stand-alone.

%package -n texlive-xypic-doc
Summary:        Documentation for xypic
Version:        svn31859.3.8.9

Provides:       tex-xypic-doc
AutoReqProv:    No

%description -n texlive-xypic-doc
Documentation for xypic

%package -n texlive-xpiano
Provides:       tex-xpiano = %{tl_version}
License:        LPPL 1.3
Summary:        An extension of the piano package
Version:        svn37604.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(xcolor.sty)
Provides:       tex(xpiano.sty) = %{tl_version}

%description -n texlive-xpiano
This package provides macros for typesetting virtual keyboards
limited to two octaves for showing notes represented by a
colored circle. Optionally, the number used for pitch analysis
can be shown. It is an extension of piano.sty by Emile
Daneault, written in expl3 in answer to a couple of questions
on TeX.StackExchange:
http://tex.stackexchange.com/questions/162184/
http://tex.stackexchange.com/questions/246276/. It features
extended syntax and several options, like setting the color,
adding numbers for pitch analysis, one or two octaves, and
others.

%package -n texlive-xpiano-doc
Summary:        Documentation for xpiano
Version:        svn37604.1.0

Provides:       tex-xpiano-doc
AutoReqProv:    No

%description -n texlive-xpiano-doc
Documentation for xpiano

%package -n texlive-xpinyin
Provides:       tex-xpinyin = %{tl_version}
License:        LPPL 1.3
Summary:        Automatically add pinyin to Chinese characters
Version:        svn46506
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(xCJK2uni.sty)
Requires:       tex(xeCJK.sty), tex(CJKutf8.sty)
Provides:       tex(xpinyin-database.def) = %{tl_version}
Provides:       tex(xpinyin.sty) = %{tl_version}

%description -n texlive-xpinyin
The package is written to simplify the input of Hanyu Pinyin.
Macros are provided that automatically add pinyin to Chinese
characters.

%package -n texlive-xpinyin-doc
Summary:        Documentation for xpinyin
Version:        svn46506
Provides:       tex-xpinyin-doc
AutoReqProv:    No

%description -n texlive-xpinyin-doc
Documentation for xpinyin

%package -n texlive-zhmetrics
Provides:       tex-zhmetrics = %{tl_version}
License:        LPPL
Summary:        TFM subfont files for using Chinese fonts in 8-bit TeX
Version:        svn22207.r206

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cyberb00.tfm) = %{tl_version}, tex(cyberb01.tfm) = %{tl_version}
Provides:       tex(cyberb02.tfm) = %{tl_version}, tex(cyberb03.tfm) = %{tl_version}
Provides:       tex(cyberb04.tfm) = %{tl_version}, tex(cyberb05.tfm) = %{tl_version}
Provides:       tex(cyberb06.tfm) = %{tl_version}, tex(cyberb07.tfm) = %{tl_version}
Provides:       tex(cyberb08.tfm) = %{tl_version}, tex(cyberb09.tfm) = %{tl_version}
Provides:       tex(cyberb0a.tfm) = %{tl_version}, tex(cyberb0b.tfm) = %{tl_version}
Provides:       tex(cyberb0c.tfm) = %{tl_version}, tex(cyberb0d.tfm) = %{tl_version}
Provides:       tex(cyberb0e.tfm) = %{tl_version}, tex(cyberb0f.tfm) = %{tl_version}
Provides:       tex(cyberb10.tfm) = %{tl_version}, tex(cyberb11.tfm) = %{tl_version}
Provides:       tex(cyberb12.tfm) = %{tl_version}, tex(cyberb13.tfm) = %{tl_version}
Provides:       tex(cyberb14.tfm) = %{tl_version}, tex(cyberb15.tfm) = %{tl_version}
Provides:       tex(cyberb16.tfm) = %{tl_version}, tex(cyberb17.tfm) = %{tl_version}
Provides:       tex(cyberb18.tfm) = %{tl_version}, tex(cyberb19.tfm) = %{tl_version}
Provides:       tex(cyberb1a.tfm) = %{tl_version}, tex(cyberb1b.tfm) = %{tl_version}
Provides:       tex(cyberb1c.tfm) = %{tl_version}, tex(cyberb1d.tfm) = %{tl_version}
Provides:       tex(cyberb1e.tfm) = %{tl_version}, tex(cyberb1f.tfm) = %{tl_version}
Provides:       tex(cyberb20.tfm) = %{tl_version}, tex(cyberb21.tfm) = %{tl_version}
Provides:       tex(cyberb22.tfm) = %{tl_version}, tex(cyberb23.tfm) = %{tl_version}
Provides:       tex(cyberb24.tfm) = %{tl_version}, tex(cyberb25.tfm) = %{tl_version}
Provides:       tex(cyberb26.tfm) = %{tl_version}, tex(cyberb27.tfm) = %{tl_version}
Provides:       tex(cyberb28.tfm) = %{tl_version}, tex(cyberb29.tfm) = %{tl_version}
Provides:       tex(cyberb2a.tfm) = %{tl_version}, tex(cyberb2b.tfm) = %{tl_version}
Provides:       tex(cyberb2c.tfm) = %{tl_version}, tex(cyberb2d.tfm) = %{tl_version}
Provides:       tex(cyberb2e.tfm) = %{tl_version}, tex(cyberb2f.tfm) = %{tl_version}
Provides:       tex(cyberb30.tfm) = %{tl_version}, tex(cyberb31.tfm) = %{tl_version}
Provides:       tex(cyberb32.tfm) = %{tl_version}, tex(cyberb33.tfm) = %{tl_version}
Provides:       tex(cyberb34.tfm) = %{tl_version}, tex(cyberb35.tfm) = %{tl_version}
Provides:       tex(cyberb36.tfm) = %{tl_version}, tex(cyberb37.tfm) = %{tl_version}
Provides:       tex(cyberb38.tfm) = %{tl_version}, tex(cyberb39.tfm) = %{tl_version}
Provides:       tex(cyberb3a.tfm) = %{tl_version}, tex(cyberb3b.tfm) = %{tl_version}
Provides:       tex(cyberb3c.tfm) = %{tl_version}, tex(cyberb3d.tfm) = %{tl_version}
Provides:       tex(cyberb3e.tfm) = %{tl_version}, tex(cyberb3f.tfm) = %{tl_version}
Provides:       tex(cyberb40.tfm) = %{tl_version}, tex(cyberb41.tfm) = %{tl_version}
Provides:       tex(cyberb42.tfm) = %{tl_version}, tex(cyberb43.tfm) = %{tl_version}
Provides:       tex(cyberb44.tfm) = %{tl_version}, tex(cyberb45.tfm) = %{tl_version}
Provides:       tex(cyberb46.tfm) = %{tl_version}, tex(cyberb47.tfm) = %{tl_version}
Provides:       tex(cyberb48.tfm) = %{tl_version}, tex(cyberb49.tfm) = %{tl_version}
Provides:       tex(cyberb4a.tfm) = %{tl_version}, tex(cyberb4b.tfm) = %{tl_version}
Provides:       tex(cyberb4c.tfm) = %{tl_version}, tex(cyberb4d.tfm) = %{tl_version}
Provides:       tex(cyberb4e.tfm) = %{tl_version}, tex(cyberb4f.tfm) = %{tl_version}
Provides:       tex(cyberb50.tfm) = %{tl_version}, tex(cyberb51.tfm) = %{tl_version}
Provides:       tex(cyberb52.tfm) = %{tl_version}, tex(cyberb53.tfm) = %{tl_version}
Provides:       tex(cyberb54.tfm) = %{tl_version}, tex(cyberb55.tfm) = %{tl_version}
Provides:       tex(cyberb56.tfm) = %{tl_version}, tex(cyberb57.tfm) = %{tl_version}
Provides:       tex(cyberb58.tfm) = %{tl_version}, tex(cyberb59.tfm) = %{tl_version}
Provides:       tex(cyberb5a.tfm) = %{tl_version}, tex(cyberb5b.tfm) = %{tl_version}
Provides:       tex(cyberb5c.tfm) = %{tl_version}, tex(cyberb5d.tfm) = %{tl_version}
Provides:       tex(cyberb5e.tfm) = %{tl_version}, tex(cyberb5f.tfm) = %{tl_version}
Provides:       tex(cyberb60.tfm) = %{tl_version}, tex(cyberb61.tfm) = %{tl_version}
Provides:       tex(cyberb62.tfm) = %{tl_version}, tex(cyberb63.tfm) = %{tl_version}
Provides:       tex(cyberb64.tfm) = %{tl_version}, tex(cyberb65.tfm) = %{tl_version}
Provides:       tex(cyberb66.tfm) = %{tl_version}, tex(cyberb67.tfm) = %{tl_version}
Provides:       tex(cyberb68.tfm) = %{tl_version}, tex(cyberb69.tfm) = %{tl_version}
Provides:       tex(cyberb6a.tfm) = %{tl_version}, tex(cyberb6b.tfm) = %{tl_version}
Provides:       tex(cyberb6c.tfm) = %{tl_version}, tex(cyberb6d.tfm) = %{tl_version}
Provides:       tex(cyberb6e.tfm) = %{tl_version}, tex(cyberb6f.tfm) = %{tl_version}
Provides:       tex(cyberb70.tfm) = %{tl_version}, tex(cyberb71.tfm) = %{tl_version}
Provides:       tex(cyberb72.tfm) = %{tl_version}, tex(cyberb73.tfm) = %{tl_version}
Provides:       tex(cyberb74.tfm) = %{tl_version}, tex(cyberb75.tfm) = %{tl_version}
Provides:       tex(cyberb76.tfm) = %{tl_version}, tex(cyberb77.tfm) = %{tl_version}
Provides:       tex(cyberb78.tfm) = %{tl_version}, tex(cyberb79.tfm) = %{tl_version}
Provides:       tex(cyberb7a.tfm) = %{tl_version}, tex(cyberb7b.tfm) = %{tl_version}
Provides:       tex(cyberb7c.tfm) = %{tl_version}, tex(cyberb7d.tfm) = %{tl_version}
Provides:       tex(cyberb7e.tfm) = %{tl_version}, tex(cyberb7f.tfm) = %{tl_version}
Provides:       tex(cyberb80.tfm) = %{tl_version}, tex(cyberb81.tfm) = %{tl_version}
Provides:       tex(cyberb82.tfm) = %{tl_version}, tex(cyberb83.tfm) = %{tl_version}
Provides:       tex(cyberb84.tfm) = %{tl_version}, tex(cyberb85.tfm) = %{tl_version}
Provides:       tex(cyberb86.tfm) = %{tl_version}, tex(cyberb87.tfm) = %{tl_version}
Provides:       tex(cyberb88.tfm) = %{tl_version}, tex(cyberb89.tfm) = %{tl_version}
Provides:       tex(cyberb8a.tfm) = %{tl_version}, tex(cyberb8b.tfm) = %{tl_version}
Provides:       tex(cyberb8c.tfm) = %{tl_version}, tex(cyberb8d.tfm) = %{tl_version}
Provides:       tex(cyberb8e.tfm) = %{tl_version}, tex(cyberb8f.tfm) = %{tl_version}
Provides:       tex(cyberb90.tfm) = %{tl_version}, tex(cyberb91.tfm) = %{tl_version}
Provides:       tex(cyberb92.tfm) = %{tl_version}, tex(cyberb93.tfm) = %{tl_version}
Provides:       tex(cyberb94.tfm) = %{tl_version}, tex(cyberb95.tfm) = %{tl_version}
Provides:       tex(cyberb96.tfm) = %{tl_version}, tex(cyberb97.tfm) = %{tl_version}
Provides:       tex(cyberb98.tfm) = %{tl_version}, tex(cyberb99.tfm) = %{tl_version}
Provides:       tex(cyberb9a.tfm) = %{tl_version}, tex(cyberb9b.tfm) = %{tl_version}
Provides:       tex(cyberb9c.tfm) = %{tl_version}, tex(cyberb9d.tfm) = %{tl_version}
Provides:       tex(cyberb9e.tfm) = %{tl_version}, tex(cyberb9f.tfm) = %{tl_version}
Provides:       tex(cyberba0.tfm) = %{tl_version}, tex(cyberba1.tfm) = %{tl_version}
Provides:       tex(cyberba2.tfm) = %{tl_version}, tex(cyberba3.tfm) = %{tl_version}
Provides:       tex(cyberba4.tfm) = %{tl_version}, tex(cyberba5.tfm) = %{tl_version}
Provides:       tex(cyberba6.tfm) = %{tl_version}, tex(cyberba7.tfm) = %{tl_version}
Provides:       tex(cyberba8.tfm) = %{tl_version}, tex(cyberba9.tfm) = %{tl_version}
Provides:       tex(cyberbaa.tfm) = %{tl_version}, tex(cyberbab.tfm) = %{tl_version}
Provides:       tex(cyberbac.tfm) = %{tl_version}, tex(cyberbad.tfm) = %{tl_version}
Provides:       tex(cyberbae.tfm) = %{tl_version}, tex(cyberbaf.tfm) = %{tl_version}
Provides:       tex(cyberbb0.tfm) = %{tl_version}, tex(cyberbb1.tfm) = %{tl_version}
Provides:       tex(cyberbb2.tfm) = %{tl_version}, tex(cyberbb3.tfm) = %{tl_version}
Provides:       tex(cyberbb4.tfm) = %{tl_version}, tex(cyberbb5.tfm) = %{tl_version}
Provides:       tex(cyberbb6.tfm) = %{tl_version}, tex(cyberbb7.tfm) = %{tl_version}
Provides:       tex(cyberbb8.tfm) = %{tl_version}, tex(cyberbb9.tfm) = %{tl_version}
Provides:       tex(cyberbba.tfm) = %{tl_version}, tex(cyberbbb.tfm) = %{tl_version}
Provides:       tex(cyberbbc.tfm) = %{tl_version}, tex(cyberbbd.tfm) = %{tl_version}
Provides:       tex(cyberbbe.tfm) = %{tl_version}, tex(cyberbbf.tfm) = %{tl_version}
Provides:       tex(cyberbc0.tfm) = %{tl_version}, tex(cyberbc1.tfm) = %{tl_version}
Provides:       tex(cyberbc2.tfm) = %{tl_version}, tex(cyberbc3.tfm) = %{tl_version}
Provides:       tex(cyberbc4.tfm) = %{tl_version}, tex(cyberbc5.tfm) = %{tl_version}
Provides:       tex(cyberbc6.tfm) = %{tl_version}, tex(cyberbc7.tfm) = %{tl_version}
Provides:       tex(cyberbc8.tfm) = %{tl_version}, tex(cyberbc9.tfm) = %{tl_version}
Provides:       tex(cyberbca.tfm) = %{tl_version}, tex(cyberbcb.tfm) = %{tl_version}
Provides:       tex(cyberbcc.tfm) = %{tl_version}, tex(cyberbcd.tfm) = %{tl_version}
Provides:       tex(cyberbce.tfm) = %{tl_version}, tex(cyberbcf.tfm) = %{tl_version}
Provides:       tex(cyberbd0.tfm) = %{tl_version}, tex(cyberbd1.tfm) = %{tl_version}
Provides:       tex(cyberbd2.tfm) = %{tl_version}, tex(cyberbd3.tfm) = %{tl_version}
Provides:       tex(cyberbd4.tfm) = %{tl_version}, tex(cyberbd5.tfm) = %{tl_version}
Provides:       tex(cyberbd6.tfm) = %{tl_version}, tex(cyberbd7.tfm) = %{tl_version}
Provides:       tex(cyberbd8.tfm) = %{tl_version}, tex(cyberbd9.tfm) = %{tl_version}
Provides:       tex(cyberbda.tfm) = %{tl_version}, tex(cyberbdb.tfm) = %{tl_version}
Provides:       tex(cyberbdc.tfm) = %{tl_version}, tex(cyberbdd.tfm) = %{tl_version}
Provides:       tex(cyberbde.tfm) = %{tl_version}, tex(cyberbdf.tfm) = %{tl_version}
Provides:       tex(cyberbe0.tfm) = %{tl_version}, tex(cyberbe1.tfm) = %{tl_version}
Provides:       tex(cyberbe2.tfm) = %{tl_version}, tex(cyberbe3.tfm) = %{tl_version}
Provides:       tex(cyberbe4.tfm) = %{tl_version}, tex(cyberbe5.tfm) = %{tl_version}
Provides:       tex(cyberbe6.tfm) = %{tl_version}, tex(cyberbe7.tfm) = %{tl_version}
Provides:       tex(cyberbe8.tfm) = %{tl_version}, tex(cyberbe9.tfm) = %{tl_version}
Provides:       tex(cyberbea.tfm) = %{tl_version}, tex(cyberbeb.tfm) = %{tl_version}
Provides:       tex(cyberbec.tfm) = %{tl_version}, tex(cyberbed.tfm) = %{tl_version}
Provides:       tex(cyberbee.tfm) = %{tl_version}, tex(cyberbef.tfm) = %{tl_version}
Provides:       tex(cyberbf0.tfm) = %{tl_version}, tex(cyberbf1.tfm) = %{tl_version}
Provides:       tex(cyberbf2.tfm) = %{tl_version}, tex(cyberbf3.tfm) = %{tl_version}
Provides:       tex(cyberbf4.tfm) = %{tl_version}, tex(cyberbf5.tfm) = %{tl_version}
Provides:       tex(cyberbf6.tfm) = %{tl_version}, tex(cyberbf7.tfm) = %{tl_version}
Provides:       tex(cyberbf8.tfm) = %{tl_version}, tex(cyberbf9.tfm) = %{tl_version}
Provides:       tex(cyberbfa.tfm) = %{tl_version}, tex(cyberbfb.tfm) = %{tl_version}
Provides:       tex(cyberbfc.tfm) = %{tl_version}, tex(cyberbfd.tfm) = %{tl_version}
Provides:       tex(cyberbfe.tfm) = %{tl_version}, tex(cyberbff.tfm) = %{tl_version}
Provides:       tex(cyberbsl00.tfm) = %{tl_version}, tex(cyberbsl01.tfm) = %{tl_version}
Provides:       tex(cyberbsl02.tfm) = %{tl_version}, tex(cyberbsl03.tfm) = %{tl_version}
Provides:       tex(cyberbsl04.tfm) = %{tl_version}, tex(cyberbsl05.tfm) = %{tl_version}
Provides:       tex(cyberbsl06.tfm) = %{tl_version}, tex(cyberbsl07.tfm) = %{tl_version}
Provides:       tex(cyberbsl08.tfm) = %{tl_version}, tex(cyberbsl09.tfm) = %{tl_version}
Provides:       tex(cyberbsl0a.tfm) = %{tl_version}, tex(cyberbsl0b.tfm) = %{tl_version}
Provides:       tex(cyberbsl0c.tfm) = %{tl_version}, tex(cyberbsl0d.tfm) = %{tl_version}
Provides:       tex(cyberbsl0e.tfm) = %{tl_version}, tex(cyberbsl0f.tfm) = %{tl_version}
Provides:       tex(cyberbsl10.tfm) = %{tl_version}, tex(cyberbsl11.tfm) = %{tl_version}
Provides:       tex(cyberbsl12.tfm) = %{tl_version}, tex(cyberbsl13.tfm) = %{tl_version}
Provides:       tex(cyberbsl14.tfm) = %{tl_version}, tex(cyberbsl15.tfm) = %{tl_version}
Provides:       tex(cyberbsl16.tfm) = %{tl_version}, tex(cyberbsl17.tfm) = %{tl_version}
Provides:       tex(cyberbsl18.tfm) = %{tl_version}, tex(cyberbsl19.tfm) = %{tl_version}
Provides:       tex(cyberbsl1a.tfm) = %{tl_version}, tex(cyberbsl1b.tfm) = %{tl_version}
Provides:       tex(cyberbsl1c.tfm) = %{tl_version}, tex(cyberbsl1d.tfm) = %{tl_version}
Provides:       tex(cyberbsl1e.tfm) = %{tl_version}, tex(cyberbsl1f.tfm) = %{tl_version}
Provides:       tex(cyberbsl20.tfm) = %{tl_version}, tex(cyberbsl21.tfm) = %{tl_version}
Provides:       tex(cyberbsl22.tfm) = %{tl_version}, tex(cyberbsl23.tfm) = %{tl_version}
Provides:       tex(cyberbsl24.tfm) = %{tl_version}, tex(cyberbsl25.tfm) = %{tl_version}
Provides:       tex(cyberbsl26.tfm) = %{tl_version}, tex(cyberbsl27.tfm) = %{tl_version}
Provides:       tex(cyberbsl28.tfm) = %{tl_version}, tex(cyberbsl29.tfm) = %{tl_version}
Provides:       tex(cyberbsl2a.tfm) = %{tl_version}, tex(cyberbsl2b.tfm) = %{tl_version}
Provides:       tex(cyberbsl2c.tfm) = %{tl_version}, tex(cyberbsl2d.tfm) = %{tl_version}
Provides:       tex(cyberbsl2e.tfm) = %{tl_version}, tex(cyberbsl2f.tfm) = %{tl_version}
Provides:       tex(cyberbsl30.tfm) = %{tl_version}, tex(cyberbsl31.tfm) = %{tl_version}
Provides:       tex(cyberbsl32.tfm) = %{tl_version}, tex(cyberbsl33.tfm) = %{tl_version}
Provides:       tex(cyberbsl34.tfm) = %{tl_version}, tex(cyberbsl35.tfm) = %{tl_version}
Provides:       tex(cyberbsl36.tfm) = %{tl_version}, tex(cyberbsl37.tfm) = %{tl_version}
Provides:       tex(cyberbsl38.tfm) = %{tl_version}, tex(cyberbsl39.tfm) = %{tl_version}
Provides:       tex(cyberbsl3a.tfm) = %{tl_version}, tex(cyberbsl3b.tfm) = %{tl_version}
Provides:       tex(cyberbsl3c.tfm) = %{tl_version}, tex(cyberbsl3d.tfm) = %{tl_version}
Provides:       tex(cyberbsl3e.tfm) = %{tl_version}, tex(cyberbsl3f.tfm) = %{tl_version}
Provides:       tex(cyberbsl40.tfm) = %{tl_version}, tex(cyberbsl41.tfm) = %{tl_version}
Provides:       tex(cyberbsl42.tfm) = %{tl_version}, tex(cyberbsl43.tfm) = %{tl_version}
Provides:       tex(cyberbsl44.tfm) = %{tl_version}, tex(cyberbsl45.tfm) = %{tl_version}
Provides:       tex(cyberbsl46.tfm) = %{tl_version}, tex(cyberbsl47.tfm) = %{tl_version}
Provides:       tex(cyberbsl48.tfm) = %{tl_version}, tex(cyberbsl49.tfm) = %{tl_version}
Provides:       tex(cyberbsl4a.tfm) = %{tl_version}, tex(cyberbsl4b.tfm) = %{tl_version}
Provides:       tex(cyberbsl4c.tfm) = %{tl_version}, tex(cyberbsl4d.tfm) = %{tl_version}
Provides:       tex(cyberbsl4e.tfm) = %{tl_version}, tex(cyberbsl4f.tfm) = %{tl_version}
Provides:       tex(cyberbsl50.tfm) = %{tl_version}, tex(cyberbsl51.tfm) = %{tl_version}
Provides:       tex(cyberbsl52.tfm) = %{tl_version}, tex(cyberbsl53.tfm) = %{tl_version}
Provides:       tex(cyberbsl54.tfm) = %{tl_version}, tex(cyberbsl55.tfm) = %{tl_version}
Provides:       tex(cyberbsl56.tfm) = %{tl_version}, tex(cyberbsl57.tfm) = %{tl_version}
Provides:       tex(cyberbsl58.tfm) = %{tl_version}, tex(cyberbsl59.tfm) = %{tl_version}
Provides:       tex(cyberbsl5a.tfm) = %{tl_version}, tex(cyberbsl5b.tfm) = %{tl_version}
Provides:       tex(cyberbsl5c.tfm) = %{tl_version}, tex(cyberbsl5d.tfm) = %{tl_version}
Provides:       tex(cyberbsl5e.tfm) = %{tl_version}, tex(cyberbsl5f.tfm) = %{tl_version}
Provides:       tex(cyberbsl60.tfm) = %{tl_version}, tex(cyberbsl61.tfm) = %{tl_version}
Provides:       tex(cyberbsl62.tfm) = %{tl_version}, tex(cyberbsl63.tfm) = %{tl_version}
Provides:       tex(cyberbsl64.tfm) = %{tl_version}, tex(cyberbsl65.tfm) = %{tl_version}
Provides:       tex(cyberbsl66.tfm) = %{tl_version}, tex(cyberbsl67.tfm) = %{tl_version}
Provides:       tex(cyberbsl68.tfm) = %{tl_version}, tex(cyberbsl69.tfm) = %{tl_version}
Provides:       tex(cyberbsl6a.tfm) = %{tl_version}, tex(cyberbsl6b.tfm) = %{tl_version}
Provides:       tex(cyberbsl6c.tfm) = %{tl_version}, tex(cyberbsl6d.tfm) = %{tl_version}
Provides:       tex(cyberbsl6e.tfm) = %{tl_version}, tex(cyberbsl6f.tfm) = %{tl_version}
Provides:       tex(cyberbsl70.tfm) = %{tl_version}, tex(cyberbsl71.tfm) = %{tl_version}
Provides:       tex(cyberbsl72.tfm) = %{tl_version}, tex(cyberbsl73.tfm) = %{tl_version}
Provides:       tex(cyberbsl74.tfm) = %{tl_version}, tex(cyberbsl75.tfm) = %{tl_version}
Provides:       tex(cyberbsl76.tfm) = %{tl_version}, tex(cyberbsl77.tfm) = %{tl_version}
Provides:       tex(cyberbsl78.tfm) = %{tl_version}, tex(cyberbsl79.tfm) = %{tl_version}
Provides:       tex(cyberbsl7a.tfm) = %{tl_version}, tex(cyberbsl7b.tfm) = %{tl_version}
Provides:       tex(cyberbsl7c.tfm) = %{tl_version}, tex(cyberbsl7d.tfm) = %{tl_version}
Provides:       tex(cyberbsl7e.tfm) = %{tl_version}, tex(cyberbsl7f.tfm) = %{tl_version}
Provides:       tex(cyberbsl80.tfm) = %{tl_version}, tex(cyberbsl81.tfm) = %{tl_version}
Provides:       tex(cyberbsl82.tfm) = %{tl_version}, tex(cyberbsl83.tfm) = %{tl_version}
Provides:       tex(cyberbsl84.tfm) = %{tl_version}, tex(cyberbsl85.tfm) = %{tl_version}
Provides:       tex(cyberbsl86.tfm) = %{tl_version}, tex(cyberbsl87.tfm) = %{tl_version}
Provides:       tex(cyberbsl88.tfm) = %{tl_version}, tex(cyberbsl89.tfm) = %{tl_version}
Provides:       tex(cyberbsl8a.tfm) = %{tl_version}, tex(cyberbsl8b.tfm) = %{tl_version}
Provides:       tex(cyberbsl8c.tfm) = %{tl_version}, tex(cyberbsl8d.tfm) = %{tl_version}
Provides:       tex(cyberbsl8e.tfm) = %{tl_version}, tex(cyberbsl8f.tfm) = %{tl_version}
Provides:       tex(cyberbsl90.tfm) = %{tl_version}, tex(cyberbsl91.tfm) = %{tl_version}
Provides:       tex(cyberbsl92.tfm) = %{tl_version}, tex(cyberbsl93.tfm) = %{tl_version}
Provides:       tex(cyberbsl94.tfm) = %{tl_version}, tex(cyberbsl95.tfm) = %{tl_version}
Provides:       tex(cyberbsl96.tfm) = %{tl_version}, tex(cyberbsl97.tfm) = %{tl_version}
Provides:       tex(cyberbsl98.tfm) = %{tl_version}, tex(cyberbsl99.tfm) = %{tl_version}
Provides:       tex(cyberbsl9a.tfm) = %{tl_version}, tex(cyberbsl9b.tfm) = %{tl_version}
Provides:       tex(cyberbsl9c.tfm) = %{tl_version}, tex(cyberbsl9d.tfm) = %{tl_version}
Provides:       tex(cyberbsl9e.tfm) = %{tl_version}, tex(cyberbsl9f.tfm) = %{tl_version}
Provides:       tex(cyberbsla0.tfm) = %{tl_version}, tex(cyberbsla1.tfm) = %{tl_version}
Provides:       tex(cyberbsla2.tfm) = %{tl_version}, tex(cyberbsla3.tfm) = %{tl_version}
Provides:       tex(cyberbsla4.tfm) = %{tl_version}, tex(cyberbsla5.tfm) = %{tl_version}
Provides:       tex(cyberbsla6.tfm) = %{tl_version}, tex(cyberbsla7.tfm) = %{tl_version}
Provides:       tex(cyberbsla8.tfm) = %{tl_version}, tex(cyberbsla9.tfm) = %{tl_version}
Provides:       tex(cyberbslaa.tfm) = %{tl_version}, tex(cyberbslab.tfm) = %{tl_version}
Provides:       tex(cyberbslac.tfm) = %{tl_version}, tex(cyberbslad.tfm) = %{tl_version}
Provides:       tex(cyberbslae.tfm) = %{tl_version}, tex(cyberbslaf.tfm) = %{tl_version}
Provides:       tex(cyberbslb0.tfm) = %{tl_version}, tex(cyberbslb1.tfm) = %{tl_version}
Provides:       tex(cyberbslb2.tfm) = %{tl_version}, tex(cyberbslb3.tfm) = %{tl_version}
Provides:       tex(cyberbslb4.tfm) = %{tl_version}, tex(cyberbslb5.tfm) = %{tl_version}
Provides:       tex(cyberbslb6.tfm) = %{tl_version}, tex(cyberbslb7.tfm) = %{tl_version}
Provides:       tex(cyberbslb8.tfm) = %{tl_version}, tex(cyberbslb9.tfm) = %{tl_version}
Provides:       tex(cyberbslba.tfm) = %{tl_version}, tex(cyberbslbb.tfm) = %{tl_version}
Provides:       tex(cyberbslbc.tfm) = %{tl_version}, tex(cyberbslbd.tfm) = %{tl_version}
Provides:       tex(cyberbslbe.tfm) = %{tl_version}, tex(cyberbslbf.tfm) = %{tl_version}
Provides:       tex(cyberbslc0.tfm) = %{tl_version}, tex(cyberbslc1.tfm) = %{tl_version}
Provides:       tex(cyberbslc2.tfm) = %{tl_version}, tex(cyberbslc3.tfm) = %{tl_version}
Provides:       tex(cyberbslc4.tfm) = %{tl_version}, tex(cyberbslc5.tfm) = %{tl_version}
Provides:       tex(cyberbslc6.tfm) = %{tl_version}, tex(cyberbslc7.tfm) = %{tl_version}
Provides:       tex(cyberbslc8.tfm) = %{tl_version}, tex(cyberbslc9.tfm) = %{tl_version}
Provides:       tex(cyberbslca.tfm) = %{tl_version}, tex(cyberbslcb.tfm) = %{tl_version}
Provides:       tex(cyberbslcc.tfm) = %{tl_version}, tex(cyberbslcd.tfm) = %{tl_version}
Provides:       tex(cyberbslce.tfm) = %{tl_version}, tex(cyberbslcf.tfm) = %{tl_version}
Provides:       tex(cyberbsld0.tfm) = %{tl_version}, tex(cyberbsld1.tfm) = %{tl_version}
Provides:       tex(cyberbsld2.tfm) = %{tl_version}, tex(cyberbsld3.tfm) = %{tl_version}
Provides:       tex(cyberbsld4.tfm) = %{tl_version}, tex(cyberbsld5.tfm) = %{tl_version}
Provides:       tex(cyberbsld6.tfm) = %{tl_version}, tex(cyberbsld7.tfm) = %{tl_version}
Provides:       tex(cyberbsld8.tfm) = %{tl_version}, tex(cyberbsld9.tfm) = %{tl_version}
Provides:       tex(cyberbslda.tfm) = %{tl_version}, tex(cyberbsldb.tfm) = %{tl_version}
Provides:       tex(cyberbsldc.tfm) = %{tl_version}, tex(cyberbsldd.tfm) = %{tl_version}
Provides:       tex(cyberbslde.tfm) = %{tl_version}, tex(cyberbsldf.tfm) = %{tl_version}
Provides:       tex(cyberbsle0.tfm) = %{tl_version}, tex(cyberbsle1.tfm) = %{tl_version}
Provides:       tex(cyberbsle2.tfm) = %{tl_version}, tex(cyberbsle3.tfm) = %{tl_version}
Provides:       tex(cyberbsle4.tfm) = %{tl_version}, tex(cyberbsle5.tfm) = %{tl_version}
Provides:       tex(cyberbsle6.tfm) = %{tl_version}, tex(cyberbsle7.tfm) = %{tl_version}
Provides:       tex(cyberbsle8.tfm) = %{tl_version}, tex(cyberbsle9.tfm) = %{tl_version}
Provides:       tex(cyberbslea.tfm) = %{tl_version}, tex(cyberbsleb.tfm) = %{tl_version}
Provides:       tex(cyberbslec.tfm) = %{tl_version}, tex(cyberbsled.tfm) = %{tl_version}
Provides:       tex(cyberbslee.tfm) = %{tl_version}, tex(cyberbslef.tfm) = %{tl_version}
Provides:       tex(cyberbslf0.tfm) = %{tl_version}, tex(cyberbslf1.tfm) = %{tl_version}
Provides:       tex(cyberbslf2.tfm) = %{tl_version}, tex(cyberbslf3.tfm) = %{tl_version}
Provides:       tex(cyberbslf4.tfm) = %{tl_version}, tex(cyberbslf5.tfm) = %{tl_version}
Provides:       tex(cyberbslf6.tfm) = %{tl_version}, tex(cyberbslf7.tfm) = %{tl_version}
Provides:       tex(cyberbslf8.tfm) = %{tl_version}, tex(cyberbslf9.tfm) = %{tl_version}
Provides:       tex(cyberbslfa.tfm) = %{tl_version}, tex(cyberbslfb.tfm) = %{tl_version}
Provides:       tex(cyberbslfc.tfm) = %{tl_version}, tex(cyberbslfd.tfm) = %{tl_version}
Provides:       tex(cyberbslfe.tfm) = %{tl_version}, tex(cyberbslff.tfm) = %{tl_version}
Provides:       tex(gbk00.tfm) = %{tl_version}, tex(gbk01.tfm) = %{tl_version}
Provides:       tex(gbk02.tfm) = %{tl_version}, tex(gbk03.tfm) = %{tl_version}
Provides:       tex(gbk04.tfm) = %{tl_version}, tex(gbk05.tfm) = %{tl_version}
Provides:       tex(gbk06.tfm) = %{tl_version}, tex(gbk07.tfm) = %{tl_version}
Provides:       tex(gbk08.tfm) = %{tl_version}, tex(gbk09.tfm) = %{tl_version}
Provides:       tex(gbk10.tfm) = %{tl_version}, tex(gbk11.tfm) = %{tl_version}
Provides:       tex(gbk12.tfm) = %{tl_version}, tex(gbk13.tfm) = %{tl_version}
Provides:       tex(gbk14.tfm) = %{tl_version}, tex(gbk15.tfm) = %{tl_version}
Provides:       tex(gbk16.tfm) = %{tl_version}, tex(gbk17.tfm) = %{tl_version}
Provides:       tex(gbk18.tfm) = %{tl_version}, tex(gbk19.tfm) = %{tl_version}
Provides:       tex(gbk20.tfm) = %{tl_version}, tex(gbk21.tfm) = %{tl_version}
Provides:       tex(gbk22.tfm) = %{tl_version}, tex(gbk23.tfm) = %{tl_version}
Provides:       tex(gbk24.tfm) = %{tl_version}, tex(gbk25.tfm) = %{tl_version}
Provides:       tex(gbk26.tfm) = %{tl_version}, tex(gbk27.tfm) = %{tl_version}
Provides:       tex(gbk28.tfm) = %{tl_version}, tex(gbk29.tfm) = %{tl_version}
Provides:       tex(gbk30.tfm) = %{tl_version}, tex(gbk31.tfm) = %{tl_version}
Provides:       tex(gbk32.tfm) = %{tl_version}, tex(gbk33.tfm) = %{tl_version}
Provides:       tex(gbk34.tfm) = %{tl_version}, tex(gbk35.tfm) = %{tl_version}
Provides:       tex(gbk36.tfm) = %{tl_version}, tex(gbk37.tfm) = %{tl_version}
Provides:       tex(gbk38.tfm) = %{tl_version}, tex(gbk39.tfm) = %{tl_version}
Provides:       tex(gbk40.tfm) = %{tl_version}, tex(gbk41.tfm) = %{tl_version}
Provides:       tex(gbk42.tfm) = %{tl_version}, tex(gbk43.tfm) = %{tl_version}
Provides:       tex(gbk44.tfm) = %{tl_version}, tex(gbk45.tfm) = %{tl_version}
Provides:       tex(gbk46.tfm) = %{tl_version}, tex(gbk47.tfm) = %{tl_version}
Provides:       tex(gbk48.tfm) = %{tl_version}, tex(gbk49.tfm) = %{tl_version}
Provides:       tex(gbk50.tfm) = %{tl_version}, tex(gbk51.tfm) = %{tl_version}
Provides:       tex(gbk52.tfm) = %{tl_version}, tex(gbk53.tfm) = %{tl_version}
Provides:       tex(gbk54.tfm) = %{tl_version}, tex(gbk55.tfm) = %{tl_version}
Provides:       tex(gbk56.tfm) = %{tl_version}, tex(gbk57.tfm) = %{tl_version}
Provides:       tex(gbk58.tfm) = %{tl_version}, tex(gbk59.tfm) = %{tl_version}
Provides:       tex(gbk60.tfm) = %{tl_version}, tex(gbk61.tfm) = %{tl_version}
Provides:       tex(gbk62.tfm) = %{tl_version}, tex(gbk63.tfm) = %{tl_version}
Provides:       tex(gbk64.tfm) = %{tl_version}, tex(gbk65.tfm) = %{tl_version}
Provides:       tex(gbk66.tfm) = %{tl_version}, tex(gbk67.tfm) = %{tl_version}
Provides:       tex(gbk68.tfm) = %{tl_version}, tex(gbk69.tfm) = %{tl_version}
Provides:       tex(gbk70.tfm) = %{tl_version}, tex(gbk71.tfm) = %{tl_version}
Provides:       tex(gbk72.tfm) = %{tl_version}, tex(gbk73.tfm) = %{tl_version}
Provides:       tex(gbk74.tfm) = %{tl_version}, tex(gbk75.tfm) = %{tl_version}
Provides:       tex(gbk76.tfm) = %{tl_version}, tex(gbk77.tfm) = %{tl_version}
Provides:       tex(gbk78.tfm) = %{tl_version}, tex(gbk79.tfm) = %{tl_version}
Provides:       tex(gbk80.tfm) = %{tl_version}, tex(gbk81.tfm) = %{tl_version}
Provides:       tex(gbk82.tfm) = %{tl_version}, tex(gbk83.tfm) = %{tl_version}
Provides:       tex(gbk84.tfm) = %{tl_version}, tex(gbk85.tfm) = %{tl_version}
Provides:       tex(gbk86.tfm) = %{tl_version}, tex(gbk87.tfm) = %{tl_version}
Provides:       tex(gbk88.tfm) = %{tl_version}, tex(gbk89.tfm) = %{tl_version}
Provides:       tex(gbk90.tfm) = %{tl_version}, tex(gbk91.tfm) = %{tl_version}
Provides:       tex(gbk92.tfm) = %{tl_version}, tex(gbk93.tfm) = %{tl_version}
Provides:       tex(gbk94.tfm) = %{tl_version}, tex(gbksl00.tfm) = %{tl_version}
Provides:       tex(gbksl01.tfm) = %{tl_version}, tex(gbksl02.tfm) = %{tl_version}
Provides:       tex(gbksl03.tfm) = %{tl_version}, tex(gbksl04.tfm) = %{tl_version}
Provides:       tex(gbksl05.tfm) = %{tl_version}, tex(gbksl06.tfm) = %{tl_version}
Provides:       tex(gbksl07.tfm) = %{tl_version}, tex(gbksl08.tfm) = %{tl_version}
Provides:       tex(gbksl09.tfm) = %{tl_version}, tex(gbksl10.tfm) = %{tl_version}
Provides:       tex(gbksl11.tfm) = %{tl_version}, tex(gbksl12.tfm) = %{tl_version}
Provides:       tex(gbksl13.tfm) = %{tl_version}, tex(gbksl14.tfm) = %{tl_version}
Provides:       tex(gbksl15.tfm) = %{tl_version}, tex(gbksl16.tfm) = %{tl_version}
Provides:       tex(gbksl17.tfm) = %{tl_version}, tex(gbksl18.tfm) = %{tl_version}
Provides:       tex(gbksl19.tfm) = %{tl_version}, tex(gbksl20.tfm) = %{tl_version}
Provides:       tex(gbksl21.tfm) = %{tl_version}, tex(gbksl22.tfm) = %{tl_version}
Provides:       tex(gbksl23.tfm) = %{tl_version}, tex(gbksl24.tfm) = %{tl_version}
Provides:       tex(gbksl25.tfm) = %{tl_version}, tex(gbksl26.tfm) = %{tl_version}
Provides:       tex(gbksl27.tfm) = %{tl_version}, tex(gbksl28.tfm) = %{tl_version}
Provides:       tex(gbksl29.tfm) = %{tl_version}, tex(gbksl30.tfm) = %{tl_version}
Provides:       tex(gbksl31.tfm) = %{tl_version}, tex(gbksl32.tfm) = %{tl_version}
Provides:       tex(gbksl33.tfm) = %{tl_version}, tex(gbksl34.tfm) = %{tl_version}
Provides:       tex(gbksl35.tfm) = %{tl_version}, tex(gbksl36.tfm) = %{tl_version}
Provides:       tex(gbksl37.tfm) = %{tl_version}, tex(gbksl38.tfm) = %{tl_version}
Provides:       tex(gbksl39.tfm) = %{tl_version}, tex(gbksl40.tfm) = %{tl_version}
Provides:       tex(gbksl41.tfm) = %{tl_version}, tex(gbksl42.tfm) = %{tl_version}
Provides:       tex(gbksl43.tfm) = %{tl_version}, tex(gbksl44.tfm) = %{tl_version}
Provides:       tex(gbksl45.tfm) = %{tl_version}, tex(gbksl46.tfm) = %{tl_version}
Provides:       tex(gbksl47.tfm) = %{tl_version}, tex(gbksl48.tfm) = %{tl_version}
Provides:       tex(gbksl49.tfm) = %{tl_version}, tex(gbksl50.tfm) = %{tl_version}
Provides:       tex(gbksl51.tfm) = %{tl_version}, tex(gbksl52.tfm) = %{tl_version}
Provides:       tex(gbksl53.tfm) = %{tl_version}, tex(gbksl54.tfm) = %{tl_version}
Provides:       tex(gbksl55.tfm) = %{tl_version}, tex(gbksl56.tfm) = %{tl_version}
Provides:       tex(gbksl57.tfm) = %{tl_version}, tex(gbksl58.tfm) = %{tl_version}
Provides:       tex(gbksl59.tfm) = %{tl_version}, tex(gbksl60.tfm) = %{tl_version}
Provides:       tex(gbksl61.tfm) = %{tl_version}, tex(gbksl62.tfm) = %{tl_version}
Provides:       tex(gbksl63.tfm) = %{tl_version}, tex(gbksl64.tfm) = %{tl_version}
Provides:       tex(gbksl65.tfm) = %{tl_version}, tex(gbksl66.tfm) = %{tl_version}
Provides:       tex(gbksl67.tfm) = %{tl_version}, tex(gbksl68.tfm) = %{tl_version}
Provides:       tex(gbksl69.tfm) = %{tl_version}, tex(gbksl70.tfm) = %{tl_version}
Provides:       tex(gbksl71.tfm) = %{tl_version}, tex(gbksl72.tfm) = %{tl_version}
Provides:       tex(gbksl73.tfm) = %{tl_version}, tex(gbksl74.tfm) = %{tl_version}
Provides:       tex(gbksl75.tfm) = %{tl_version}, tex(gbksl76.tfm) = %{tl_version}
Provides:       tex(gbksl77.tfm) = %{tl_version}, tex(gbksl78.tfm) = %{tl_version}
Provides:       tex(gbksl79.tfm) = %{tl_version}, tex(gbksl80.tfm) = %{tl_version}
Provides:       tex(gbksl81.tfm) = %{tl_version}, tex(gbksl82.tfm) = %{tl_version}
Provides:       tex(gbksl83.tfm) = %{tl_version}, tex(gbksl84.tfm) = %{tl_version}
Provides:       tex(gbksl85.tfm) = %{tl_version}, tex(gbksl86.tfm) = %{tl_version}
Provides:       tex(gbksl87.tfm) = %{tl_version}, tex(gbksl88.tfm) = %{tl_version}
Provides:       tex(gbksl89.tfm) = %{tl_version}, tex(gbksl90.tfm) = %{tl_version}
Provides:       tex(gbksl91.tfm) = %{tl_version}, tex(gbksl92.tfm) = %{tl_version}
Provides:       tex(gbksl93.tfm) = %{tl_version}, tex(gbksl94.tfm) = %{tl_version}
Provides:       tex(gbkfs00.tfm) = %{tl_version}, tex(gbkfs01.tfm) = %{tl_version}
Provides:       tex(gbkfs02.tfm) = %{tl_version}, tex(gbkfs03.tfm) = %{tl_version}
Provides:       tex(gbkfs04.tfm) = %{tl_version}, tex(gbkfs05.tfm) = %{tl_version}
Provides:       tex(gbkfs06.tfm) = %{tl_version}, tex(gbkfs07.tfm) = %{tl_version}
Provides:       tex(gbkfs08.tfm) = %{tl_version}, tex(gbkfs09.tfm) = %{tl_version}
Provides:       tex(gbkfs10.tfm) = %{tl_version}, tex(gbkfs11.tfm) = %{tl_version}
Provides:       tex(gbkfs12.tfm) = %{tl_version}, tex(gbkfs13.tfm) = %{tl_version}
Provides:       tex(gbkfs14.tfm) = %{tl_version}, tex(gbkfs15.tfm) = %{tl_version}
Provides:       tex(gbkfs16.tfm) = %{tl_version}, tex(gbkfs17.tfm) = %{tl_version}
Provides:       tex(gbkfs18.tfm) = %{tl_version}, tex(gbkfs19.tfm) = %{tl_version}
Provides:       tex(gbkfs20.tfm) = %{tl_version}, tex(gbkfs21.tfm) = %{tl_version}
Provides:       tex(gbkfs22.tfm) = %{tl_version}, tex(gbkfs23.tfm) = %{tl_version}
Provides:       tex(gbkfs24.tfm) = %{tl_version}, tex(gbkfs25.tfm) = %{tl_version}
Provides:       tex(gbkfs26.tfm) = %{tl_version}, tex(gbkfs27.tfm) = %{tl_version}
Provides:       tex(gbkfs28.tfm) = %{tl_version}, tex(gbkfs29.tfm) = %{tl_version}
Provides:       tex(gbkfs30.tfm) = %{tl_version}, tex(gbkfs31.tfm) = %{tl_version}
Provides:       tex(gbkfs32.tfm) = %{tl_version}, tex(gbkfs33.tfm) = %{tl_version}
Provides:       tex(gbkfs34.tfm) = %{tl_version}, tex(gbkfs35.tfm) = %{tl_version}
Provides:       tex(gbkfs36.tfm) = %{tl_version}, tex(gbkfs37.tfm) = %{tl_version}
Provides:       tex(gbkfs38.tfm) = %{tl_version}, tex(gbkfs39.tfm) = %{tl_version}
Provides:       tex(gbkfs40.tfm) = %{tl_version}, tex(gbkfs41.tfm) = %{tl_version}
Provides:       tex(gbkfs42.tfm) = %{tl_version}, tex(gbkfs43.tfm) = %{tl_version}
Provides:       tex(gbkfs44.tfm) = %{tl_version}, tex(gbkfs45.tfm) = %{tl_version}
Provides:       tex(gbkfs46.tfm) = %{tl_version}, tex(gbkfs47.tfm) = %{tl_version}
Provides:       tex(gbkfs48.tfm) = %{tl_version}, tex(gbkfs49.tfm) = %{tl_version}
Provides:       tex(gbkfs50.tfm) = %{tl_version}, tex(gbkfs51.tfm) = %{tl_version}
Provides:       tex(gbkfs52.tfm) = %{tl_version}, tex(gbkfs53.tfm) = %{tl_version}
Provides:       tex(gbkfs54.tfm) = %{tl_version}, tex(gbkfs55.tfm) = %{tl_version}
Provides:       tex(gbkfs56.tfm) = %{tl_version}, tex(gbkfs57.tfm) = %{tl_version}
Provides:       tex(gbkfs58.tfm) = %{tl_version}, tex(gbkfs59.tfm) = %{tl_version}
Provides:       tex(gbkfs60.tfm) = %{tl_version}, tex(gbkfs61.tfm) = %{tl_version}
Provides:       tex(gbkfs62.tfm) = %{tl_version}, tex(gbkfs63.tfm) = %{tl_version}
Provides:       tex(gbkfs64.tfm) = %{tl_version}, tex(gbkfs65.tfm) = %{tl_version}
Provides:       tex(gbkfs66.tfm) = %{tl_version}, tex(gbkfs67.tfm) = %{tl_version}
Provides:       tex(gbkfs68.tfm) = %{tl_version}, tex(gbkfs69.tfm) = %{tl_version}
Provides:       tex(gbkfs70.tfm) = %{tl_version}, tex(gbkfs71.tfm) = %{tl_version}
Provides:       tex(gbkfs72.tfm) = %{tl_version}, tex(gbkfs73.tfm) = %{tl_version}
Provides:       tex(gbkfs74.tfm) = %{tl_version}, tex(gbkfs75.tfm) = %{tl_version}
Provides:       tex(gbkfs76.tfm) = %{tl_version}, tex(gbkfs77.tfm) = %{tl_version}
Provides:       tex(gbkfs78.tfm) = %{tl_version}, tex(gbkfs79.tfm) = %{tl_version}
Provides:       tex(gbkfs80.tfm) = %{tl_version}, tex(gbkfs81.tfm) = %{tl_version}
Provides:       tex(gbkfs82.tfm) = %{tl_version}, tex(gbkfs83.tfm) = %{tl_version}
Provides:       tex(gbkfs84.tfm) = %{tl_version}, tex(gbkfs85.tfm) = %{tl_version}
Provides:       tex(gbkfs86.tfm) = %{tl_version}, tex(gbkfs87.tfm) = %{tl_version}
Provides:       tex(gbkfs88.tfm) = %{tl_version}, tex(gbkfs89.tfm) = %{tl_version}
Provides:       tex(gbkfs90.tfm) = %{tl_version}, tex(gbkfs91.tfm) = %{tl_version}
Provides:       tex(gbkfs92.tfm) = %{tl_version}, tex(gbkfs93.tfm) = %{tl_version}
Provides:       tex(gbkfs94.tfm) = %{tl_version}, tex(gbkfssl00.tfm) = %{tl_version}
Provides:       tex(gbkfssl01.tfm) = %{tl_version}, tex(gbkfssl02.tfm) = %{tl_version}
Provides:       tex(gbkfssl03.tfm) = %{tl_version}, tex(gbkfssl04.tfm) = %{tl_version}
Provides:       tex(gbkfssl05.tfm) = %{tl_version}, tex(gbkfssl06.tfm) = %{tl_version}
Provides:       tex(gbkfssl07.tfm) = %{tl_version}, tex(gbkfssl08.tfm) = %{tl_version}
Provides:       tex(gbkfssl09.tfm) = %{tl_version}, tex(gbkfssl10.tfm) = %{tl_version}
Provides:       tex(gbkfssl11.tfm) = %{tl_version}, tex(gbkfssl12.tfm) = %{tl_version}
Provides:       tex(gbkfssl13.tfm) = %{tl_version}, tex(gbkfssl14.tfm) = %{tl_version}
Provides:       tex(gbkfssl15.tfm) = %{tl_version}, tex(gbkfssl16.tfm) = %{tl_version}
Provides:       tex(gbkfssl17.tfm) = %{tl_version}, tex(gbkfssl18.tfm) = %{tl_version}
Provides:       tex(gbkfssl19.tfm) = %{tl_version}, tex(gbkfssl20.tfm) = %{tl_version}
Provides:       tex(gbkfssl21.tfm) = %{tl_version}, tex(gbkfssl22.tfm) = %{tl_version}
Provides:       tex(gbkfssl23.tfm) = %{tl_version}, tex(gbkfssl24.tfm) = %{tl_version}
Provides:       tex(gbkfssl25.tfm) = %{tl_version}, tex(gbkfssl26.tfm) = %{tl_version}
Provides:       tex(gbkfssl27.tfm) = %{tl_version}, tex(gbkfssl28.tfm) = %{tl_version}
Provides:       tex(gbkfssl29.tfm) = %{tl_version}, tex(gbkfssl30.tfm) = %{tl_version}
Provides:       tex(gbkfssl31.tfm) = %{tl_version}, tex(gbkfssl32.tfm) = %{tl_version}
Provides:       tex(gbkfssl33.tfm) = %{tl_version}, tex(gbkfssl34.tfm) = %{tl_version}
Provides:       tex(gbkfssl35.tfm) = %{tl_version}, tex(gbkfssl36.tfm) = %{tl_version}
Provides:       tex(gbkfssl37.tfm) = %{tl_version}, tex(gbkfssl38.tfm) = %{tl_version}
Provides:       tex(gbkfssl39.tfm) = %{tl_version}, tex(gbkfssl40.tfm) = %{tl_version}
Provides:       tex(gbkfssl41.tfm) = %{tl_version}, tex(gbkfssl42.tfm) = %{tl_version}
Provides:       tex(gbkfssl43.tfm) = %{tl_version}, tex(gbkfssl44.tfm) = %{tl_version}
Provides:       tex(gbkfssl45.tfm) = %{tl_version}, tex(gbkfssl46.tfm) = %{tl_version}
Provides:       tex(gbkfssl47.tfm) = %{tl_version}, tex(gbkfssl48.tfm) = %{tl_version}
Provides:       tex(gbkfssl49.tfm) = %{tl_version}, tex(gbkfssl50.tfm) = %{tl_version}
Provides:       tex(gbkfssl51.tfm) = %{tl_version}, tex(gbkfssl52.tfm) = %{tl_version}
Provides:       tex(gbkfssl53.tfm) = %{tl_version}, tex(gbkfssl54.tfm) = %{tl_version}
Provides:       tex(gbkfssl55.tfm) = %{tl_version}, tex(gbkfssl56.tfm) = %{tl_version}
Provides:       tex(gbkfssl57.tfm) = %{tl_version}, tex(gbkfssl58.tfm) = %{tl_version}
Provides:       tex(gbkfssl59.tfm) = %{tl_version}, tex(gbkfssl60.tfm) = %{tl_version}
Provides:       tex(gbkfssl61.tfm) = %{tl_version}, tex(gbkfssl62.tfm) = %{tl_version}
Provides:       tex(gbkfssl63.tfm) = %{tl_version}, tex(gbkfssl64.tfm) = %{tl_version}
Provides:       tex(gbkfssl65.tfm) = %{tl_version}, tex(gbkfssl66.tfm) = %{tl_version}
Provides:       tex(gbkfssl67.tfm) = %{tl_version}, tex(gbkfssl68.tfm) = %{tl_version}
Provides:       tex(gbkfssl69.tfm) = %{tl_version}, tex(gbkfssl70.tfm) = %{tl_version}
Provides:       tex(gbkfssl71.tfm) = %{tl_version}, tex(gbkfssl72.tfm) = %{tl_version}
Provides:       tex(gbkfssl73.tfm) = %{tl_version}, tex(gbkfssl74.tfm) = %{tl_version}
Provides:       tex(gbkfssl75.tfm) = %{tl_version}, tex(gbkfssl76.tfm) = %{tl_version}
Provides:       tex(gbkfssl77.tfm) = %{tl_version}, tex(gbkfssl78.tfm) = %{tl_version}
Provides:       tex(gbkfssl79.tfm) = %{tl_version}, tex(gbkfssl80.tfm) = %{tl_version}
Provides:       tex(gbkfssl81.tfm) = %{tl_version}, tex(gbkfssl82.tfm) = %{tl_version}
Provides:       tex(gbkfssl83.tfm) = %{tl_version}, tex(gbkfssl84.tfm) = %{tl_version}
Provides:       tex(gbkfssl85.tfm) = %{tl_version}, tex(gbkfssl86.tfm) = %{tl_version}
Provides:       tex(gbkfssl87.tfm) = %{tl_version}, tex(gbkfssl88.tfm) = %{tl_version}
Provides:       tex(gbkfssl89.tfm) = %{tl_version}, tex(gbkfssl90.tfm) = %{tl_version}
Provides:       tex(gbkfssl91.tfm) = %{tl_version}, tex(gbkfssl92.tfm) = %{tl_version}
Provides:       tex(gbkfssl93.tfm) = %{tl_version}, tex(gbkfssl94.tfm) = %{tl_version}
Provides:       tex(gbkhei00.tfm) = %{tl_version}, tex(gbkhei01.tfm) = %{tl_version}
Provides:       tex(gbkhei02.tfm) = %{tl_version}, tex(gbkhei03.tfm) = %{tl_version}
Provides:       tex(gbkhei04.tfm) = %{tl_version}, tex(gbkhei05.tfm) = %{tl_version}
Provides:       tex(gbkhei06.tfm) = %{tl_version}, tex(gbkhei07.tfm) = %{tl_version}
Provides:       tex(gbkhei08.tfm) = %{tl_version}, tex(gbkhei09.tfm) = %{tl_version}
Provides:       tex(gbkhei10.tfm) = %{tl_version}, tex(gbkhei11.tfm) = %{tl_version}
Provides:       tex(gbkhei12.tfm) = %{tl_version}, tex(gbkhei13.tfm) = %{tl_version}
Provides:       tex(gbkhei14.tfm) = %{tl_version}, tex(gbkhei15.tfm) = %{tl_version}
Provides:       tex(gbkhei16.tfm) = %{tl_version}, tex(gbkhei17.tfm) = %{tl_version}
Provides:       tex(gbkhei18.tfm) = %{tl_version}, tex(gbkhei19.tfm) = %{tl_version}
Provides:       tex(gbkhei20.tfm) = %{tl_version}, tex(gbkhei21.tfm) = %{tl_version}
Provides:       tex(gbkhei22.tfm) = %{tl_version}, tex(gbkhei23.tfm) = %{tl_version}
Provides:       tex(gbkhei24.tfm) = %{tl_version}, tex(gbkhei25.tfm) = %{tl_version}
Provides:       tex(gbkhei26.tfm) = %{tl_version}, tex(gbkhei27.tfm) = %{tl_version}
Provides:       tex(gbkhei28.tfm) = %{tl_version}, tex(gbkhei29.tfm) = %{tl_version}
Provides:       tex(gbkhei30.tfm) = %{tl_version}, tex(gbkhei31.tfm) = %{tl_version}
Provides:       tex(gbkhei32.tfm) = %{tl_version}, tex(gbkhei33.tfm) = %{tl_version}
Provides:       tex(gbkhei34.tfm) = %{tl_version}, tex(gbkhei35.tfm) = %{tl_version}
Provides:       tex(gbkhei36.tfm) = %{tl_version}, tex(gbkhei37.tfm) = %{tl_version}
Provides:       tex(gbkhei38.tfm) = %{tl_version}, tex(gbkhei39.tfm) = %{tl_version}
Provides:       tex(gbkhei40.tfm) = %{tl_version}, tex(gbkhei41.tfm) = %{tl_version}
Provides:       tex(gbkhei42.tfm) = %{tl_version}, tex(gbkhei43.tfm) = %{tl_version}
Provides:       tex(gbkhei44.tfm) = %{tl_version}, tex(gbkhei45.tfm) = %{tl_version}
Provides:       tex(gbkhei46.tfm) = %{tl_version}, tex(gbkhei47.tfm) = %{tl_version}
Provides:       tex(gbkhei48.tfm) = %{tl_version}, tex(gbkhei49.tfm) = %{tl_version}
Provides:       tex(gbkhei50.tfm) = %{tl_version}, tex(gbkhei51.tfm) = %{tl_version}
Provides:       tex(gbkhei52.tfm) = %{tl_version}, tex(gbkhei53.tfm) = %{tl_version}
Provides:       tex(gbkhei54.tfm) = %{tl_version}, tex(gbkhei55.tfm) = %{tl_version}
Provides:       tex(gbkhei56.tfm) = %{tl_version}, tex(gbkhei57.tfm) = %{tl_version}
Provides:       tex(gbkhei58.tfm) = %{tl_version}, tex(gbkhei59.tfm) = %{tl_version}
Provides:       tex(gbkhei60.tfm) = %{tl_version}, tex(gbkhei61.tfm) = %{tl_version}
Provides:       tex(gbkhei62.tfm) = %{tl_version}, tex(gbkhei63.tfm) = %{tl_version}
Provides:       tex(gbkhei64.tfm) = %{tl_version}, tex(gbkhei65.tfm) = %{tl_version}
Provides:       tex(gbkhei66.tfm) = %{tl_version}, tex(gbkhei67.tfm) = %{tl_version}
Provides:       tex(gbkhei68.tfm) = %{tl_version}, tex(gbkhei69.tfm) = %{tl_version}
Provides:       tex(gbkhei70.tfm) = %{tl_version}, tex(gbkhei71.tfm) = %{tl_version}
Provides:       tex(gbkhei72.tfm) = %{tl_version}, tex(gbkhei73.tfm) = %{tl_version}
Provides:       tex(gbkhei74.tfm) = %{tl_version}, tex(gbkhei75.tfm) = %{tl_version}
Provides:       tex(gbkhei76.tfm) = %{tl_version}, tex(gbkhei77.tfm) = %{tl_version}
Provides:       tex(gbkhei78.tfm) = %{tl_version}, tex(gbkhei79.tfm) = %{tl_version}
Provides:       tex(gbkhei80.tfm) = %{tl_version}, tex(gbkhei81.tfm) = %{tl_version}
Provides:       tex(gbkhei82.tfm) = %{tl_version}, tex(gbkhei83.tfm) = %{tl_version}
Provides:       tex(gbkhei84.tfm) = %{tl_version}, tex(gbkhei85.tfm) = %{tl_version}
Provides:       tex(gbkhei86.tfm) = %{tl_version}, tex(gbkhei87.tfm) = %{tl_version}
Provides:       tex(gbkhei88.tfm) = %{tl_version}, tex(gbkhei89.tfm) = %{tl_version}
Provides:       tex(gbkhei90.tfm) = %{tl_version}, tex(gbkhei91.tfm) = %{tl_version}
Provides:       tex(gbkhei92.tfm) = %{tl_version}, tex(gbkhei93.tfm) = %{tl_version}
Provides:       tex(gbkhei94.tfm) = %{tl_version}, tex(gbkheisl00.tfm) = %{tl_version}
Provides:       tex(gbkheisl01.tfm) = %{tl_version}, tex(gbkheisl02.tfm) = %{tl_version}
Provides:       tex(gbkheisl03.tfm) = %{tl_version}, tex(gbkheisl04.tfm) = %{tl_version}
Provides:       tex(gbkheisl05.tfm) = %{tl_version}, tex(gbkheisl06.tfm) = %{tl_version}
Provides:       tex(gbkheisl07.tfm) = %{tl_version}, tex(gbkheisl08.tfm) = %{tl_version}
Provides:       tex(gbkheisl09.tfm) = %{tl_version}, tex(gbkheisl10.tfm) = %{tl_version}
Provides:       tex(gbkheisl11.tfm) = %{tl_version}, tex(gbkheisl12.tfm) = %{tl_version}
Provides:       tex(gbkheisl13.tfm) = %{tl_version}, tex(gbkheisl14.tfm) = %{tl_version}
Provides:       tex(gbkheisl15.tfm) = %{tl_version}, tex(gbkheisl16.tfm) = %{tl_version}
Provides:       tex(gbkheisl17.tfm) = %{tl_version}, tex(gbkheisl18.tfm) = %{tl_version}
Provides:       tex(gbkheisl19.tfm) = %{tl_version}, tex(gbkheisl20.tfm) = %{tl_version}
Provides:       tex(gbkheisl21.tfm) = %{tl_version}, tex(gbkheisl22.tfm) = %{tl_version}
Provides:       tex(gbkheisl23.tfm) = %{tl_version}, tex(gbkheisl24.tfm) = %{tl_version}
Provides:       tex(gbkheisl25.tfm) = %{tl_version}, tex(gbkheisl26.tfm) = %{tl_version}
Provides:       tex(gbkheisl27.tfm) = %{tl_version}, tex(gbkheisl28.tfm) = %{tl_version}
Provides:       tex(gbkheisl29.tfm) = %{tl_version}, tex(gbkheisl30.tfm) = %{tl_version}
Provides:       tex(gbkheisl31.tfm) = %{tl_version}, tex(gbkheisl32.tfm) = %{tl_version}
Provides:       tex(gbkheisl33.tfm) = %{tl_version}, tex(gbkheisl34.tfm) = %{tl_version}
Provides:       tex(gbkheisl35.tfm) = %{tl_version}, tex(gbkheisl36.tfm) = %{tl_version}
Provides:       tex(gbkheisl37.tfm) = %{tl_version}, tex(gbkheisl38.tfm) = %{tl_version}
Provides:       tex(gbkheisl39.tfm) = %{tl_version}, tex(gbkheisl40.tfm) = %{tl_version}
Provides:       tex(gbkheisl41.tfm) = %{tl_version}, tex(gbkheisl42.tfm) = %{tl_version}
Provides:       tex(gbkheisl43.tfm) = %{tl_version}, tex(gbkheisl44.tfm) = %{tl_version}
Provides:       tex(gbkheisl45.tfm) = %{tl_version}, tex(gbkheisl46.tfm) = %{tl_version}
Provides:       tex(gbkheisl47.tfm) = %{tl_version}, tex(gbkheisl48.tfm) = %{tl_version}
Provides:       tex(gbkheisl49.tfm) = %{tl_version}, tex(gbkheisl50.tfm) = %{tl_version}
Provides:       tex(gbkheisl51.tfm) = %{tl_version}, tex(gbkheisl52.tfm) = %{tl_version}
Provides:       tex(gbkheisl53.tfm) = %{tl_version}, tex(gbkheisl54.tfm) = %{tl_version}
Provides:       tex(gbkheisl55.tfm) = %{tl_version}, tex(gbkheisl56.tfm) = %{tl_version}
Provides:       tex(gbkheisl57.tfm) = %{tl_version}, tex(gbkheisl58.tfm) = %{tl_version}
Provides:       tex(gbkheisl59.tfm) = %{tl_version}, tex(gbkheisl60.tfm) = %{tl_version}
Provides:       tex(gbkheisl61.tfm) = %{tl_version}, tex(gbkheisl62.tfm) = %{tl_version}
Provides:       tex(gbkheisl63.tfm) = %{tl_version}, tex(gbkheisl64.tfm) = %{tl_version}
Provides:       tex(gbkheisl65.tfm) = %{tl_version}, tex(gbkheisl66.tfm) = %{tl_version}
Provides:       tex(gbkheisl67.tfm) = %{tl_version}, tex(gbkheisl68.tfm) = %{tl_version}
Provides:       tex(gbkheisl69.tfm) = %{tl_version}, tex(gbkheisl70.tfm) = %{tl_version}
Provides:       tex(gbkheisl71.tfm) = %{tl_version}, tex(gbkheisl72.tfm) = %{tl_version}
Provides:       tex(gbkheisl73.tfm) = %{tl_version}, tex(gbkheisl74.tfm) = %{tl_version}
Provides:       tex(gbkheisl75.tfm) = %{tl_version}, tex(gbkheisl76.tfm) = %{tl_version}
Provides:       tex(gbkheisl77.tfm) = %{tl_version}, tex(gbkheisl78.tfm) = %{tl_version}
Provides:       tex(gbkheisl79.tfm) = %{tl_version}, tex(gbkheisl80.tfm) = %{tl_version}
Provides:       tex(gbkheisl81.tfm) = %{tl_version}, tex(gbkheisl82.tfm) = %{tl_version}
Provides:       tex(gbkheisl83.tfm) = %{tl_version}, tex(gbkheisl84.tfm) = %{tl_version}
Provides:       tex(gbkheisl85.tfm) = %{tl_version}, tex(gbkheisl86.tfm) = %{tl_version}
Provides:       tex(gbkheisl87.tfm) = %{tl_version}, tex(gbkheisl88.tfm) = %{tl_version}
Provides:       tex(gbkheisl89.tfm) = %{tl_version}, tex(gbkheisl90.tfm) = %{tl_version}
Provides:       tex(gbkheisl91.tfm) = %{tl_version}, tex(gbkheisl92.tfm) = %{tl_version}
Provides:       tex(gbkheisl93.tfm) = %{tl_version}, tex(gbkheisl94.tfm) = %{tl_version}
Provides:       tex(gbkkai00.tfm) = %{tl_version}, tex(gbkkai01.tfm) = %{tl_version}
Provides:       tex(gbkkai02.tfm) = %{tl_version}, tex(gbkkai03.tfm) = %{tl_version}
Provides:       tex(gbkkai04.tfm) = %{tl_version}, tex(gbkkai05.tfm) = %{tl_version}
Provides:       tex(gbkkai06.tfm) = %{tl_version}, tex(gbkkai07.tfm) = %{tl_version}
Provides:       tex(gbkkai08.tfm) = %{tl_version}, tex(gbkkai09.tfm) = %{tl_version}
Provides:       tex(gbkkai10.tfm) = %{tl_version}, tex(gbkkai11.tfm) = %{tl_version}
Provides:       tex(gbkkai12.tfm) = %{tl_version}, tex(gbkkai13.tfm) = %{tl_version}
Provides:       tex(gbkkai14.tfm) = %{tl_version}, tex(gbkkai15.tfm) = %{tl_version}
Provides:       tex(gbkkai16.tfm) = %{tl_version}, tex(gbkkai17.tfm) = %{tl_version}
Provides:       tex(gbkkai18.tfm) = %{tl_version}, tex(gbkkai19.tfm) = %{tl_version}
Provides:       tex(gbkkai20.tfm) = %{tl_version}, tex(gbkkai21.tfm) = %{tl_version}
Provides:       tex(gbkkai22.tfm) = %{tl_version}, tex(gbkkai23.tfm) = %{tl_version}
Provides:       tex(gbkkai24.tfm) = %{tl_version}, tex(gbkkai25.tfm) = %{tl_version}
Provides:       tex(gbkkai26.tfm) = %{tl_version}, tex(gbkkai27.tfm) = %{tl_version}
Provides:       tex(gbkkai28.tfm) = %{tl_version}, tex(gbkkai29.tfm) = %{tl_version}
Provides:       tex(gbkkai30.tfm) = %{tl_version}, tex(gbkkai31.tfm) = %{tl_version}
Provides:       tex(gbkkai32.tfm) = %{tl_version}, tex(gbkkai33.tfm) = %{tl_version}
Provides:       tex(gbkkai34.tfm) = %{tl_version}, tex(gbkkai35.tfm) = %{tl_version}
Provides:       tex(gbkkai36.tfm) = %{tl_version}, tex(gbkkai37.tfm) = %{tl_version}
Provides:       tex(gbkkai38.tfm) = %{tl_version}, tex(gbkkai39.tfm) = %{tl_version}
Provides:       tex(gbkkai40.tfm) = %{tl_version}, tex(gbkkai41.tfm) = %{tl_version}
Provides:       tex(gbkkai42.tfm) = %{tl_version}, tex(gbkkai43.tfm) = %{tl_version}
Provides:       tex(gbkkai44.tfm) = %{tl_version}, tex(gbkkai45.tfm) = %{tl_version}
Provides:       tex(gbkkai46.tfm) = %{tl_version}, tex(gbkkai47.tfm) = %{tl_version}
Provides:       tex(gbkkai48.tfm) = %{tl_version}, tex(gbkkai49.tfm) = %{tl_version}
Provides:       tex(gbkkai50.tfm) = %{tl_version}, tex(gbkkai51.tfm) = %{tl_version}
Provides:       tex(gbkkai52.tfm) = %{tl_version}, tex(gbkkai53.tfm) = %{tl_version}
Provides:       tex(gbkkai54.tfm) = %{tl_version}, tex(gbkkai55.tfm) = %{tl_version}
Provides:       tex(gbkkai56.tfm) = %{tl_version}, tex(gbkkai57.tfm) = %{tl_version}
Provides:       tex(gbkkai58.tfm) = %{tl_version}, tex(gbkkai59.tfm) = %{tl_version}
Provides:       tex(gbkkai60.tfm) = %{tl_version}, tex(gbkkai61.tfm) = %{tl_version}
Provides:       tex(gbkkai62.tfm) = %{tl_version}, tex(gbkkai63.tfm) = %{tl_version}
Provides:       tex(gbkkai64.tfm) = %{tl_version}, tex(gbkkai65.tfm) = %{tl_version}
Provides:       tex(gbkkai66.tfm) = %{tl_version}, tex(gbkkai67.tfm) = %{tl_version}
Provides:       tex(gbkkai68.tfm) = %{tl_version}, tex(gbkkai69.tfm) = %{tl_version}
Provides:       tex(gbkkai70.tfm) = %{tl_version}, tex(gbkkai71.tfm) = %{tl_version}
Provides:       tex(gbkkai72.tfm) = %{tl_version}, tex(gbkkai73.tfm) = %{tl_version}
Provides:       tex(gbkkai74.tfm) = %{tl_version}, tex(gbkkai75.tfm) = %{tl_version}
Provides:       tex(gbkkai76.tfm) = %{tl_version}, tex(gbkkai77.tfm) = %{tl_version}
Provides:       tex(gbkkai78.tfm) = %{tl_version}, tex(gbkkai79.tfm) = %{tl_version}
Provides:       tex(gbkkai80.tfm) = %{tl_version}, tex(gbkkai81.tfm) = %{tl_version}
Provides:       tex(gbkkai82.tfm) = %{tl_version}, tex(gbkkai83.tfm) = %{tl_version}
Provides:       tex(gbkkai84.tfm) = %{tl_version}, tex(gbkkai85.tfm) = %{tl_version}
Provides:       tex(gbkkai86.tfm) = %{tl_version}, tex(gbkkai87.tfm) = %{tl_version}
Provides:       tex(gbkkai88.tfm) = %{tl_version}, tex(gbkkai89.tfm) = %{tl_version}
Provides:       tex(gbkkai90.tfm) = %{tl_version}, tex(gbkkai91.tfm) = %{tl_version}
Provides:       tex(gbkkai92.tfm) = %{tl_version}, tex(gbkkai93.tfm) = %{tl_version}
Provides:       tex(gbkkai94.tfm) = %{tl_version}, tex(gbkkaisl00.tfm) = %{tl_version}
Provides:       tex(gbkkaisl01.tfm) = %{tl_version}, tex(gbkkaisl02.tfm) = %{tl_version}
Provides:       tex(gbkkaisl03.tfm) = %{tl_version}, tex(gbkkaisl04.tfm) = %{tl_version}
Provides:       tex(gbkkaisl05.tfm) = %{tl_version}, tex(gbkkaisl06.tfm) = %{tl_version}
Provides:       tex(gbkkaisl07.tfm) = %{tl_version}, tex(gbkkaisl08.tfm) = %{tl_version}
Provides:       tex(gbkkaisl09.tfm) = %{tl_version}, tex(gbkkaisl10.tfm) = %{tl_version}
Provides:       tex(gbkkaisl11.tfm) = %{tl_version}, tex(gbkkaisl12.tfm) = %{tl_version}
Provides:       tex(gbkkaisl13.tfm) = %{tl_version}, tex(gbkkaisl14.tfm) = %{tl_version}
Provides:       tex(gbkkaisl15.tfm) = %{tl_version}, tex(gbkkaisl16.tfm) = %{tl_version}
Provides:       tex(gbkkaisl17.tfm) = %{tl_version}, tex(gbkkaisl18.tfm) = %{tl_version}
Provides:       tex(gbkkaisl19.tfm) = %{tl_version}, tex(gbkkaisl20.tfm) = %{tl_version}
Provides:       tex(gbkkaisl21.tfm) = %{tl_version}, tex(gbkkaisl22.tfm) = %{tl_version}
Provides:       tex(gbkkaisl23.tfm) = %{tl_version}, tex(gbkkaisl24.tfm) = %{tl_version}
Provides:       tex(gbkkaisl25.tfm) = %{tl_version}, tex(gbkkaisl26.tfm) = %{tl_version}
Provides:       tex(gbkkaisl27.tfm) = %{tl_version}, tex(gbkkaisl28.tfm) = %{tl_version}
Provides:       tex(gbkkaisl29.tfm) = %{tl_version}, tex(gbkkaisl30.tfm) = %{tl_version}
Provides:       tex(gbkkaisl31.tfm) = %{tl_version}, tex(gbkkaisl32.tfm) = %{tl_version}
Provides:       tex(gbkkaisl33.tfm) = %{tl_version}, tex(gbkkaisl34.tfm) = %{tl_version}
Provides:       tex(gbkkaisl35.tfm) = %{tl_version}, tex(gbkkaisl36.tfm) = %{tl_version}
Provides:       tex(gbkkaisl37.tfm) = %{tl_version}, tex(gbkkaisl38.tfm) = %{tl_version}
Provides:       tex(gbkkaisl39.tfm) = %{tl_version}, tex(gbkkaisl40.tfm) = %{tl_version}
Provides:       tex(gbkkaisl41.tfm) = %{tl_version}, tex(gbkkaisl42.tfm) = %{tl_version}
Provides:       tex(gbkkaisl43.tfm) = %{tl_version}, tex(gbkkaisl44.tfm) = %{tl_version}
Provides:       tex(gbkkaisl45.tfm) = %{tl_version}, tex(gbkkaisl46.tfm) = %{tl_version}
Provides:       tex(gbkkaisl47.tfm) = %{tl_version}, tex(gbkkaisl48.tfm) = %{tl_version}
Provides:       tex(gbkkaisl49.tfm) = %{tl_version}, tex(gbkkaisl50.tfm) = %{tl_version}
Provides:       tex(gbkkaisl51.tfm) = %{tl_version}, tex(gbkkaisl52.tfm) = %{tl_version}
Provides:       tex(gbkkaisl53.tfm) = %{tl_version}, tex(gbkkaisl54.tfm) = %{tl_version}
Provides:       tex(gbkkaisl55.tfm) = %{tl_version}, tex(gbkkaisl56.tfm) = %{tl_version}
Provides:       tex(gbkkaisl57.tfm) = %{tl_version}, tex(gbkkaisl58.tfm) = %{tl_version}
Provides:       tex(gbkkaisl59.tfm) = %{tl_version}, tex(gbkkaisl60.tfm) = %{tl_version}
Provides:       tex(gbkkaisl61.tfm) = %{tl_version}, tex(gbkkaisl62.tfm) = %{tl_version}
Provides:       tex(gbkkaisl63.tfm) = %{tl_version}, tex(gbkkaisl64.tfm) = %{tl_version}
Provides:       tex(gbkkaisl65.tfm) = %{tl_version}, tex(gbkkaisl66.tfm) = %{tl_version}
Provides:       tex(gbkkaisl67.tfm) = %{tl_version}, tex(gbkkaisl68.tfm) = %{tl_version}
Provides:       tex(gbkkaisl69.tfm) = %{tl_version}, tex(gbkkaisl70.tfm) = %{tl_version}
Provides:       tex(gbkkaisl71.tfm) = %{tl_version}, tex(gbkkaisl72.tfm) = %{tl_version}
Provides:       tex(gbkkaisl73.tfm) = %{tl_version}, tex(gbkkaisl74.tfm) = %{tl_version}
Provides:       tex(gbkkaisl75.tfm) = %{tl_version}, tex(gbkkaisl76.tfm) = %{tl_version}
Provides:       tex(gbkkaisl77.tfm) = %{tl_version}, tex(gbkkaisl78.tfm) = %{tl_version}
Provides:       tex(gbkkaisl79.tfm) = %{tl_version}, tex(gbkkaisl80.tfm) = %{tl_version}
Provides:       tex(gbkkaisl81.tfm) = %{tl_version}, tex(gbkkaisl82.tfm) = %{tl_version}
Provides:       tex(gbkkaisl83.tfm) = %{tl_version}, tex(gbkkaisl84.tfm) = %{tl_version}
Provides:       tex(gbkkaisl85.tfm) = %{tl_version}, tex(gbkkaisl86.tfm) = %{tl_version}
Provides:       tex(gbkkaisl87.tfm) = %{tl_version}, tex(gbkkaisl88.tfm) = %{tl_version}
Provides:       tex(gbkkaisl89.tfm) = %{tl_version}, tex(gbkkaisl90.tfm) = %{tl_version}
Provides:       tex(gbkkaisl91.tfm) = %{tl_version}, tex(gbkkaisl92.tfm) = %{tl_version}
Provides:       tex(gbkkaisl93.tfm) = %{tl_version}, tex(gbkkaisl94.tfm) = %{tl_version}
Provides:       tex(gbkli00.tfm) = %{tl_version}, tex(gbkli01.tfm) = %{tl_version}
Provides:       tex(gbkli02.tfm) = %{tl_version}, tex(gbkli03.tfm) = %{tl_version}
Provides:       tex(gbkli04.tfm) = %{tl_version}, tex(gbkli05.tfm) = %{tl_version}
Provides:       tex(gbkli06.tfm) = %{tl_version}, tex(gbkli07.tfm) = %{tl_version}
Provides:       tex(gbkli08.tfm) = %{tl_version}, tex(gbkli09.tfm) = %{tl_version}
Provides:       tex(gbkli10.tfm) = %{tl_version}, tex(gbkli11.tfm) = %{tl_version}
Provides:       tex(gbkli12.tfm) = %{tl_version}, tex(gbkli13.tfm) = %{tl_version}
Provides:       tex(gbkli14.tfm) = %{tl_version}, tex(gbkli15.tfm) = %{tl_version}
Provides:       tex(gbkli16.tfm) = %{tl_version}, tex(gbkli17.tfm) = %{tl_version}
Provides:       tex(gbkli18.tfm) = %{tl_version}, tex(gbkli19.tfm) = %{tl_version}
Provides:       tex(gbkli20.tfm) = %{tl_version}, tex(gbkli21.tfm) = %{tl_version}
Provides:       tex(gbkli22.tfm) = %{tl_version}, tex(gbkli23.tfm) = %{tl_version}
Provides:       tex(gbkli24.tfm) = %{tl_version}, tex(gbkli25.tfm) = %{tl_version}
Provides:       tex(gbkli26.tfm) = %{tl_version}, tex(gbkli27.tfm) = %{tl_version}
Provides:       tex(gbkli28.tfm) = %{tl_version}, tex(gbkli29.tfm) = %{tl_version}
Provides:       tex(gbkli30.tfm) = %{tl_version}, tex(gbkli31.tfm) = %{tl_version}
Provides:       tex(gbkli32.tfm) = %{tl_version}, tex(gbkli33.tfm) = %{tl_version}
Provides:       tex(gbkli34.tfm) = %{tl_version}, tex(gbkli35.tfm) = %{tl_version}
Provides:       tex(gbkli36.tfm) = %{tl_version}, tex(gbkli37.tfm) = %{tl_version}
Provides:       tex(gbkli38.tfm) = %{tl_version}, tex(gbkli39.tfm) = %{tl_version}
Provides:       tex(gbkli40.tfm) = %{tl_version}, tex(gbkli41.tfm) = %{tl_version}
Provides:       tex(gbkli42.tfm) = %{tl_version}, tex(gbkli43.tfm) = %{tl_version}
Provides:       tex(gbkli44.tfm) = %{tl_version}, tex(gbkli45.tfm) = %{tl_version}
Provides:       tex(gbkli46.tfm) = %{tl_version}, tex(gbkli47.tfm) = %{tl_version}
Provides:       tex(gbkli48.tfm) = %{tl_version}, tex(gbkli49.tfm) = %{tl_version}
Provides:       tex(gbkli50.tfm) = %{tl_version}, tex(gbkli51.tfm) = %{tl_version}
Provides:       tex(gbkli52.tfm) = %{tl_version}, tex(gbkli53.tfm) = %{tl_version}
Provides:       tex(gbkli54.tfm) = %{tl_version}, tex(gbkli55.tfm) = %{tl_version}
Provides:       tex(gbkli56.tfm) = %{tl_version}, tex(gbkli57.tfm) = %{tl_version}
Provides:       tex(gbkli58.tfm) = %{tl_version}, tex(gbkli59.tfm) = %{tl_version}
Provides:       tex(gbkli60.tfm) = %{tl_version}, tex(gbkli61.tfm) = %{tl_version}
Provides:       tex(gbkli62.tfm) = %{tl_version}, tex(gbkli63.tfm) = %{tl_version}
Provides:       tex(gbkli64.tfm) = %{tl_version}, tex(gbkli65.tfm) = %{tl_version}
Provides:       tex(gbkli66.tfm) = %{tl_version}, tex(gbkli67.tfm) = %{tl_version}
Provides:       tex(gbkli68.tfm) = %{tl_version}, tex(gbkli69.tfm) = %{tl_version}
Provides:       tex(gbkli70.tfm) = %{tl_version}, tex(gbkli71.tfm) = %{tl_version}
Provides:       tex(gbkli72.tfm) = %{tl_version}, tex(gbkli73.tfm) = %{tl_version}
Provides:       tex(gbkli74.tfm) = %{tl_version}, tex(gbkli75.tfm) = %{tl_version}
Provides:       tex(gbkli76.tfm) = %{tl_version}, tex(gbkli77.tfm) = %{tl_version}
Provides:       tex(gbkli78.tfm) = %{tl_version}, tex(gbkli79.tfm) = %{tl_version}
Provides:       tex(gbkli80.tfm) = %{tl_version}, tex(gbkli81.tfm) = %{tl_version}
Provides:       tex(gbkli82.tfm) = %{tl_version}, tex(gbkli83.tfm) = %{tl_version}
Provides:       tex(gbkli84.tfm) = %{tl_version}, tex(gbkli85.tfm) = %{tl_version}
Provides:       tex(gbkli86.tfm) = %{tl_version}, tex(gbkli87.tfm) = %{tl_version}
Provides:       tex(gbkli88.tfm) = %{tl_version}, tex(gbkli89.tfm) = %{tl_version}
Provides:       tex(gbkli90.tfm) = %{tl_version}, tex(gbkli91.tfm) = %{tl_version}
Provides:       tex(gbkli92.tfm) = %{tl_version}, tex(gbkli93.tfm) = %{tl_version}
Provides:       tex(gbkli94.tfm) = %{tl_version}, tex(gbklisl00.tfm) = %{tl_version}
Provides:       tex(gbklisl01.tfm) = %{tl_version}, tex(gbklisl02.tfm) = %{tl_version}
Provides:       tex(gbklisl03.tfm) = %{tl_version}, tex(gbklisl04.tfm) = %{tl_version}
Provides:       tex(gbklisl05.tfm) = %{tl_version}, tex(gbklisl06.tfm) = %{tl_version}
Provides:       tex(gbklisl07.tfm) = %{tl_version}, tex(gbklisl08.tfm) = %{tl_version}
Provides:       tex(gbklisl09.tfm) = %{tl_version}, tex(gbklisl10.tfm) = %{tl_version}
Provides:       tex(gbklisl11.tfm) = %{tl_version}, tex(gbklisl12.tfm) = %{tl_version}
Provides:       tex(gbklisl13.tfm) = %{tl_version}, tex(gbklisl14.tfm) = %{tl_version}
Provides:       tex(gbklisl15.tfm) = %{tl_version}, tex(gbklisl16.tfm) = %{tl_version}
Provides:       tex(gbklisl17.tfm) = %{tl_version}, tex(gbklisl18.tfm) = %{tl_version}
Provides:       tex(gbklisl19.tfm) = %{tl_version}, tex(gbklisl20.tfm) = %{tl_version}
Provides:       tex(gbklisl21.tfm) = %{tl_version}, tex(gbklisl22.tfm) = %{tl_version}
Provides:       tex(gbklisl23.tfm) = %{tl_version}, tex(gbklisl24.tfm) = %{tl_version}
Provides:       tex(gbklisl25.tfm) = %{tl_version}, tex(gbklisl26.tfm) = %{tl_version}
Provides:       tex(gbklisl27.tfm) = %{tl_version}, tex(gbklisl28.tfm) = %{tl_version}
Provides:       tex(gbklisl29.tfm) = %{tl_version}, tex(gbklisl30.tfm) = %{tl_version}
Provides:       tex(gbklisl31.tfm) = %{tl_version}, tex(gbklisl32.tfm) = %{tl_version}
Provides:       tex(gbklisl33.tfm) = %{tl_version}, tex(gbklisl34.tfm) = %{tl_version}
Provides:       tex(gbklisl35.tfm) = %{tl_version}, tex(gbklisl36.tfm) = %{tl_version}
Provides:       tex(gbklisl37.tfm) = %{tl_version}, tex(gbklisl38.tfm) = %{tl_version}
Provides:       tex(gbklisl39.tfm) = %{tl_version}, tex(gbklisl40.tfm) = %{tl_version}
Provides:       tex(gbklisl41.tfm) = %{tl_version}, tex(gbklisl42.tfm) = %{tl_version}
Provides:       tex(gbklisl43.tfm) = %{tl_version}, tex(gbklisl44.tfm) = %{tl_version}
Provides:       tex(gbklisl45.tfm) = %{tl_version}, tex(gbklisl46.tfm) = %{tl_version}
Provides:       tex(gbklisl47.tfm) = %{tl_version}, tex(gbklisl48.tfm) = %{tl_version}
Provides:       tex(gbklisl49.tfm) = %{tl_version}, tex(gbklisl50.tfm) = %{tl_version}
Provides:       tex(gbklisl51.tfm) = %{tl_version}, tex(gbklisl52.tfm) = %{tl_version}
Provides:       tex(gbklisl53.tfm) = %{tl_version}, tex(gbklisl54.tfm) = %{tl_version}
Provides:       tex(gbklisl55.tfm) = %{tl_version}, tex(gbklisl56.tfm) = %{tl_version}
Provides:       tex(gbklisl57.tfm) = %{tl_version}, tex(gbklisl58.tfm) = %{tl_version}
Provides:       tex(gbklisl59.tfm) = %{tl_version}, tex(gbklisl60.tfm) = %{tl_version}
Provides:       tex(gbklisl61.tfm) = %{tl_version}, tex(gbklisl62.tfm) = %{tl_version}
Provides:       tex(gbklisl63.tfm) = %{tl_version}, tex(gbklisl64.tfm) = %{tl_version}
Provides:       tex(gbklisl65.tfm) = %{tl_version}, tex(gbklisl66.tfm) = %{tl_version}
Provides:       tex(gbklisl67.tfm) = %{tl_version}, tex(gbklisl68.tfm) = %{tl_version}
Provides:       tex(gbklisl69.tfm) = %{tl_version}, tex(gbklisl70.tfm) = %{tl_version}
Provides:       tex(gbklisl71.tfm) = %{tl_version}, tex(gbklisl72.tfm) = %{tl_version}
Provides:       tex(gbklisl73.tfm) = %{tl_version}, tex(gbklisl74.tfm) = %{tl_version}
Provides:       tex(gbklisl75.tfm) = %{tl_version}, tex(gbklisl76.tfm) = %{tl_version}
Provides:       tex(gbklisl77.tfm) = %{tl_version}, tex(gbklisl78.tfm) = %{tl_version}
Provides:       tex(gbklisl79.tfm) = %{tl_version}, tex(gbklisl80.tfm) = %{tl_version}
Provides:       tex(gbklisl81.tfm) = %{tl_version}, tex(gbklisl82.tfm) = %{tl_version}
Provides:       tex(gbklisl83.tfm) = %{tl_version}, tex(gbklisl84.tfm) = %{tl_version}
Provides:       tex(gbklisl85.tfm) = %{tl_version}, tex(gbklisl86.tfm) = %{tl_version}
Provides:       tex(gbklisl87.tfm) = %{tl_version}, tex(gbklisl88.tfm) = %{tl_version}
Provides:       tex(gbklisl89.tfm) = %{tl_version}, tex(gbklisl90.tfm) = %{tl_version}
Provides:       tex(gbklisl91.tfm) = %{tl_version}, tex(gbklisl92.tfm) = %{tl_version}
Provides:       tex(gbklisl93.tfm) = %{tl_version}, tex(gbklisl94.tfm) = %{tl_version}
Provides:       tex(gbksong00.tfm) = %{tl_version}, tex(gbksong01.tfm) = %{tl_version}
Provides:       tex(gbksong02.tfm) = %{tl_version}, tex(gbksong03.tfm) = %{tl_version}
Provides:       tex(gbksong04.tfm) = %{tl_version}, tex(gbksong05.tfm) = %{tl_version}
Provides:       tex(gbksong06.tfm) = %{tl_version}, tex(gbksong07.tfm) = %{tl_version}
Provides:       tex(gbksong08.tfm) = %{tl_version}, tex(gbksong09.tfm) = %{tl_version}
Provides:       tex(gbksong10.tfm) = %{tl_version}, tex(gbksong11.tfm) = %{tl_version}
Provides:       tex(gbksong12.tfm) = %{tl_version}, tex(gbksong13.tfm) = %{tl_version}
Provides:       tex(gbksong14.tfm) = %{tl_version}, tex(gbksong15.tfm) = %{tl_version}
Provides:       tex(gbksong16.tfm) = %{tl_version}, tex(gbksong17.tfm) = %{tl_version}
Provides:       tex(gbksong18.tfm) = %{tl_version}, tex(gbksong19.tfm) = %{tl_version}
Provides:       tex(gbksong20.tfm) = %{tl_version}, tex(gbksong21.tfm) = %{tl_version}
Provides:       tex(gbksong22.tfm) = %{tl_version}, tex(gbksong23.tfm) = %{tl_version}
Provides:       tex(gbksong24.tfm) = %{tl_version}, tex(gbksong25.tfm) = %{tl_version}
Provides:       tex(gbksong26.tfm) = %{tl_version}, tex(gbksong27.tfm) = %{tl_version}
Provides:       tex(gbksong28.tfm) = %{tl_version}, tex(gbksong29.tfm) = %{tl_version}
Provides:       tex(gbksong30.tfm) = %{tl_version}, tex(gbksong31.tfm) = %{tl_version}
Provides:       tex(gbksong32.tfm) = %{tl_version}, tex(gbksong33.tfm) = %{tl_version}
Provides:       tex(gbksong34.tfm) = %{tl_version}, tex(gbksong35.tfm) = %{tl_version}
Provides:       tex(gbksong36.tfm) = %{tl_version}, tex(gbksong37.tfm) = %{tl_version}
Provides:       tex(gbksong38.tfm) = %{tl_version}, tex(gbksong39.tfm) = %{tl_version}
Provides:       tex(gbksong40.tfm) = %{tl_version}, tex(gbksong41.tfm) = %{tl_version}
Provides:       tex(gbksong42.tfm) = %{tl_version}, tex(gbksong43.tfm) = %{tl_version}
Provides:       tex(gbksong44.tfm) = %{tl_version}, tex(gbksong45.tfm) = %{tl_version}
Provides:       tex(gbksong46.tfm) = %{tl_version}, tex(gbksong47.tfm) = %{tl_version}
Provides:       tex(gbksong48.tfm) = %{tl_version}, tex(gbksong49.tfm) = %{tl_version}
Provides:       tex(gbksong50.tfm) = %{tl_version}, tex(gbksong51.tfm) = %{tl_version}
Provides:       tex(gbksong52.tfm) = %{tl_version}, tex(gbksong53.tfm) = %{tl_version}
Provides:       tex(gbksong54.tfm) = %{tl_version}, tex(gbksong55.tfm) = %{tl_version}
Provides:       tex(gbksong56.tfm) = %{tl_version}, tex(gbksong57.tfm) = %{tl_version}
Provides:       tex(gbksong58.tfm) = %{tl_version}, tex(gbksong59.tfm) = %{tl_version}
Provides:       tex(gbksong60.tfm) = %{tl_version}, tex(gbksong61.tfm) = %{tl_version}
Provides:       tex(gbksong62.tfm) = %{tl_version}, tex(gbksong63.tfm) = %{tl_version}
Provides:       tex(gbksong64.tfm) = %{tl_version}, tex(gbksong65.tfm) = %{tl_version}
Provides:       tex(gbksong66.tfm) = %{tl_version}, tex(gbksong67.tfm) = %{tl_version}
Provides:       tex(gbksong68.tfm) = %{tl_version}, tex(gbksong69.tfm) = %{tl_version}
Provides:       tex(gbksong70.tfm) = %{tl_version}, tex(gbksong71.tfm) = %{tl_version}
Provides:       tex(gbksong72.tfm) = %{tl_version}, tex(gbksong73.tfm) = %{tl_version}
Provides:       tex(gbksong74.tfm) = %{tl_version}, tex(gbksong75.tfm) = %{tl_version}
Provides:       tex(gbksong76.tfm) = %{tl_version}, tex(gbksong77.tfm) = %{tl_version}
Provides:       tex(gbksong78.tfm) = %{tl_version}, tex(gbksong79.tfm) = %{tl_version}
Provides:       tex(gbksong80.tfm) = %{tl_version}, tex(gbksong81.tfm) = %{tl_version}
Provides:       tex(gbksong82.tfm) = %{tl_version}, tex(gbksong83.tfm) = %{tl_version}
Provides:       tex(gbksong84.tfm) = %{tl_version}, tex(gbksong85.tfm) = %{tl_version}
Provides:       tex(gbksong86.tfm) = %{tl_version}, tex(gbksong87.tfm) = %{tl_version}
Provides:       tex(gbksong88.tfm) = %{tl_version}, tex(gbksong89.tfm) = %{tl_version}
Provides:       tex(gbksong90.tfm) = %{tl_version}, tex(gbksong91.tfm) = %{tl_version}
Provides:       tex(gbksong92.tfm) = %{tl_version}, tex(gbksong93.tfm) = %{tl_version}
Provides:       tex(gbksong94.tfm) = %{tl_version}, tex(gbksongsl00.tfm) = %{tl_version}
Provides:       tex(gbksongsl01.tfm) = %{tl_version}, tex(gbksongsl02.tfm) = %{tl_version}
Provides:       tex(gbksongsl03.tfm) = %{tl_version}, tex(gbksongsl04.tfm) = %{tl_version}
Provides:       tex(gbksongsl05.tfm) = %{tl_version}, tex(gbksongsl06.tfm) = %{tl_version}
Provides:       tex(gbksongsl07.tfm) = %{tl_version}, tex(gbksongsl08.tfm) = %{tl_version}
Provides:       tex(gbksongsl09.tfm) = %{tl_version}, tex(gbksongsl10.tfm) = %{tl_version}
Provides:       tex(gbksongsl11.tfm) = %{tl_version}, tex(gbksongsl12.tfm) = %{tl_version}
Provides:       tex(gbksongsl13.tfm) = %{tl_version}, tex(gbksongsl14.tfm) = %{tl_version}
Provides:       tex(gbksongsl15.tfm) = %{tl_version}, tex(gbksongsl16.tfm) = %{tl_version}
Provides:       tex(gbksongsl17.tfm) = %{tl_version}, tex(gbksongsl18.tfm) = %{tl_version}
Provides:       tex(gbksongsl19.tfm) = %{tl_version}, tex(gbksongsl20.tfm) = %{tl_version}
Provides:       tex(gbksongsl21.tfm) = %{tl_version}, tex(gbksongsl22.tfm) = %{tl_version}
Provides:       tex(gbksongsl23.tfm) = %{tl_version}, tex(gbksongsl24.tfm) = %{tl_version}
Provides:       tex(gbksongsl25.tfm) = %{tl_version}, tex(gbksongsl26.tfm) = %{tl_version}
Provides:       tex(gbksongsl27.tfm) = %{tl_version}, tex(gbksongsl28.tfm) = %{tl_version}
Provides:       tex(gbksongsl29.tfm) = %{tl_version}, tex(gbksongsl30.tfm) = %{tl_version}
Provides:       tex(gbksongsl31.tfm) = %{tl_version}, tex(gbksongsl32.tfm) = %{tl_version}
Provides:       tex(gbksongsl33.tfm) = %{tl_version}, tex(gbksongsl34.tfm) = %{tl_version}
Provides:       tex(gbksongsl35.tfm) = %{tl_version}, tex(gbksongsl36.tfm) = %{tl_version}
Provides:       tex(gbksongsl37.tfm) = %{tl_version}, tex(gbksongsl38.tfm) = %{tl_version}
Provides:       tex(gbksongsl39.tfm) = %{tl_version}, tex(gbksongsl40.tfm) = %{tl_version}
Provides:       tex(gbksongsl41.tfm) = %{tl_version}, tex(gbksongsl42.tfm) = %{tl_version}
Provides:       tex(gbksongsl43.tfm) = %{tl_version}, tex(gbksongsl44.tfm) = %{tl_version}
Provides:       tex(gbksongsl45.tfm) = %{tl_version}, tex(gbksongsl46.tfm) = %{tl_version}
Provides:       tex(gbksongsl47.tfm) = %{tl_version}, tex(gbksongsl48.tfm) = %{tl_version}
Provides:       tex(gbksongsl49.tfm) = %{tl_version}, tex(gbksongsl50.tfm) = %{tl_version}
Provides:       tex(gbksongsl51.tfm) = %{tl_version}, tex(gbksongsl52.tfm) = %{tl_version}
Provides:       tex(gbksongsl53.tfm) = %{tl_version}, tex(gbksongsl54.tfm) = %{tl_version}
Provides:       tex(gbksongsl55.tfm) = %{tl_version}, tex(gbksongsl56.tfm) = %{tl_version}
Provides:       tex(gbksongsl57.tfm) = %{tl_version}, tex(gbksongsl58.tfm) = %{tl_version}
Provides:       tex(gbksongsl59.tfm) = %{tl_version}, tex(gbksongsl60.tfm) = %{tl_version}
Provides:       tex(gbksongsl61.tfm) = %{tl_version}, tex(gbksongsl62.tfm) = %{tl_version}
Provides:       tex(gbksongsl63.tfm) = %{tl_version}, tex(gbksongsl64.tfm) = %{tl_version}
Provides:       tex(gbksongsl65.tfm) = %{tl_version}, tex(gbksongsl66.tfm) = %{tl_version}
Provides:       tex(gbksongsl67.tfm) = %{tl_version}, tex(gbksongsl68.tfm) = %{tl_version}
Provides:       tex(gbksongsl69.tfm) = %{tl_version}, tex(gbksongsl70.tfm) = %{tl_version}
Provides:       tex(gbksongsl71.tfm) = %{tl_version}, tex(gbksongsl72.tfm) = %{tl_version}
Provides:       tex(gbksongsl73.tfm) = %{tl_version}, tex(gbksongsl74.tfm) = %{tl_version}
Provides:       tex(gbksongsl75.tfm) = %{tl_version}, tex(gbksongsl76.tfm) = %{tl_version}
Provides:       tex(gbksongsl77.tfm) = %{tl_version}, tex(gbksongsl78.tfm) = %{tl_version}
Provides:       tex(gbksongsl79.tfm) = %{tl_version}, tex(gbksongsl80.tfm) = %{tl_version}
Provides:       tex(gbksongsl81.tfm) = %{tl_version}, tex(gbksongsl82.tfm) = %{tl_version}
Provides:       tex(gbksongsl83.tfm) = %{tl_version}, tex(gbksongsl84.tfm) = %{tl_version}
Provides:       tex(gbksongsl85.tfm) = %{tl_version}, tex(gbksongsl86.tfm) = %{tl_version}
Provides:       tex(gbksongsl87.tfm) = %{tl_version}, tex(gbksongsl88.tfm) = %{tl_version}
Provides:       tex(gbksongsl89.tfm) = %{tl_version}, tex(gbksongsl90.tfm) = %{tl_version}
Provides:       tex(gbksongsl91.tfm) = %{tl_version}, tex(gbksongsl92.tfm) = %{tl_version}
Provides:       tex(gbksongsl93.tfm) = %{tl_version}, tex(gbksongsl94.tfm) = %{tl_version}
Provides:       tex(gbkyou00.tfm) = %{tl_version}, tex(gbkyou01.tfm) = %{tl_version}
Provides:       tex(gbkyou02.tfm) = %{tl_version}, tex(gbkyou03.tfm) = %{tl_version}
Provides:       tex(gbkyou04.tfm) = %{tl_version}, tex(gbkyou05.tfm) = %{tl_version}
Provides:       tex(gbkyou06.tfm) = %{tl_version}, tex(gbkyou07.tfm) = %{tl_version}
Provides:       tex(gbkyou08.tfm) = %{tl_version}, tex(gbkyou09.tfm) = %{tl_version}
Provides:       tex(gbkyou10.tfm) = %{tl_version}, tex(gbkyou11.tfm) = %{tl_version}
Provides:       tex(gbkyou12.tfm) = %{tl_version}, tex(gbkyou13.tfm) = %{tl_version}
Provides:       tex(gbkyou14.tfm) = %{tl_version}, tex(gbkyou15.tfm) = %{tl_version}
Provides:       tex(gbkyou16.tfm) = %{tl_version}, tex(gbkyou17.tfm) = %{tl_version}
Provides:       tex(gbkyou18.tfm) = %{tl_version}, tex(gbkyou19.tfm) = %{tl_version}
Provides:       tex(gbkyou20.tfm) = %{tl_version}, tex(gbkyou21.tfm) = %{tl_version}
Provides:       tex(gbkyou22.tfm) = %{tl_version}, tex(gbkyou23.tfm) = %{tl_version}
Provides:       tex(gbkyou24.tfm) = %{tl_version}, tex(gbkyou25.tfm) = %{tl_version}
Provides:       tex(gbkyou26.tfm) = %{tl_version}, tex(gbkyou27.tfm) = %{tl_version}
Provides:       tex(gbkyou28.tfm) = %{tl_version}, tex(gbkyou29.tfm) = %{tl_version}
Provides:       tex(gbkyou30.tfm) = %{tl_version}, tex(gbkyou31.tfm) = %{tl_version}
Provides:       tex(gbkyou32.tfm) = %{tl_version}, tex(gbkyou33.tfm) = %{tl_version}
Provides:       tex(gbkyou34.tfm) = %{tl_version}, tex(gbkyou35.tfm) = %{tl_version}
Provides:       tex(gbkyou36.tfm) = %{tl_version}, tex(gbkyou37.tfm) = %{tl_version}
Provides:       tex(gbkyou38.tfm) = %{tl_version}, tex(gbkyou39.tfm) = %{tl_version}
Provides:       tex(gbkyou40.tfm) = %{tl_version}, tex(gbkyou41.tfm) = %{tl_version}
Provides:       tex(gbkyou42.tfm) = %{tl_version}, tex(gbkyou43.tfm) = %{tl_version}
Provides:       tex(gbkyou44.tfm) = %{tl_version}, tex(gbkyou45.tfm) = %{tl_version}
Provides:       tex(gbkyou46.tfm) = %{tl_version}, tex(gbkyou47.tfm) = %{tl_version}
Provides:       tex(gbkyou48.tfm) = %{tl_version}, tex(gbkyou49.tfm) = %{tl_version}
Provides:       tex(gbkyou50.tfm) = %{tl_version}, tex(gbkyou51.tfm) = %{tl_version}
Provides:       tex(gbkyou52.tfm) = %{tl_version}, tex(gbkyou53.tfm) = %{tl_version}
Provides:       tex(gbkyou54.tfm) = %{tl_version}, tex(gbkyou55.tfm) = %{tl_version}
Provides:       tex(gbkyou56.tfm) = %{tl_version}, tex(gbkyou57.tfm) = %{tl_version}
Provides:       tex(gbkyou58.tfm) = %{tl_version}, tex(gbkyou59.tfm) = %{tl_version}
Provides:       tex(gbkyou60.tfm) = %{tl_version}, tex(gbkyou61.tfm) = %{tl_version}
Provides:       tex(gbkyou62.tfm) = %{tl_version}, tex(gbkyou63.tfm) = %{tl_version}
Provides:       tex(gbkyou64.tfm) = %{tl_version}, tex(gbkyou65.tfm) = %{tl_version}
Provides:       tex(gbkyou66.tfm) = %{tl_version}, tex(gbkyou67.tfm) = %{tl_version}
Provides:       tex(gbkyou68.tfm) = %{tl_version}, tex(gbkyou69.tfm) = %{tl_version}
Provides:       tex(gbkyou70.tfm) = %{tl_version}, tex(gbkyou71.tfm) = %{tl_version}
Provides:       tex(gbkyou72.tfm) = %{tl_version}, tex(gbkyou73.tfm) = %{tl_version}
Provides:       tex(gbkyou74.tfm) = %{tl_version}, tex(gbkyou75.tfm) = %{tl_version}
Provides:       tex(gbkyou76.tfm) = %{tl_version}, tex(gbkyou77.tfm) = %{tl_version}
Provides:       tex(gbkyou78.tfm) = %{tl_version}, tex(gbkyou79.tfm) = %{tl_version}
Provides:       tex(gbkyou80.tfm) = %{tl_version}, tex(gbkyou81.tfm) = %{tl_version}
Provides:       tex(gbkyou82.tfm) = %{tl_version}, tex(gbkyou83.tfm) = %{tl_version}
Provides:       tex(gbkyou84.tfm) = %{tl_version}, tex(gbkyou85.tfm) = %{tl_version}
Provides:       tex(gbkyou86.tfm) = %{tl_version}, tex(gbkyou87.tfm) = %{tl_version}
Provides:       tex(gbkyou88.tfm) = %{tl_version}, tex(gbkyou89.tfm) = %{tl_version}
Provides:       tex(gbkyou90.tfm) = %{tl_version}, tex(gbkyou91.tfm) = %{tl_version}
Provides:       tex(gbkyou92.tfm) = %{tl_version}, tex(gbkyou93.tfm) = %{tl_version}
Provides:       tex(gbkyou94.tfm) = %{tl_version}, tex(gbkyousl00.tfm) = %{tl_version}
Provides:       tex(gbkyousl01.tfm) = %{tl_version}, tex(gbkyousl02.tfm) = %{tl_version}
Provides:       tex(gbkyousl03.tfm) = %{tl_version}, tex(gbkyousl04.tfm) = %{tl_version}
Provides:       tex(gbkyousl05.tfm) = %{tl_version}, tex(gbkyousl06.tfm) = %{tl_version}
Provides:       tex(gbkyousl07.tfm) = %{tl_version}, tex(gbkyousl08.tfm) = %{tl_version}
Provides:       tex(gbkyousl09.tfm) = %{tl_version}, tex(gbkyousl10.tfm) = %{tl_version}
Provides:       tex(gbkyousl11.tfm) = %{tl_version}, tex(gbkyousl12.tfm) = %{tl_version}
Provides:       tex(gbkyousl13.tfm) = %{tl_version}, tex(gbkyousl14.tfm) = %{tl_version}
Provides:       tex(gbkyousl15.tfm) = %{tl_version}, tex(gbkyousl16.tfm) = %{tl_version}
Provides:       tex(gbkyousl17.tfm) = %{tl_version}, tex(gbkyousl18.tfm) = %{tl_version}
Provides:       tex(gbkyousl19.tfm) = %{tl_version}, tex(gbkyousl20.tfm) = %{tl_version}
Provides:       tex(gbkyousl21.tfm) = %{tl_version}, tex(gbkyousl22.tfm) = %{tl_version}
Provides:       tex(gbkyousl23.tfm) = %{tl_version}, tex(gbkyousl24.tfm) = %{tl_version}
Provides:       tex(gbkyousl25.tfm) = %{tl_version}, tex(gbkyousl26.tfm) = %{tl_version}
Provides:       tex(gbkyousl27.tfm) = %{tl_version}, tex(gbkyousl28.tfm) = %{tl_version}
Provides:       tex(gbkyousl29.tfm) = %{tl_version}, tex(gbkyousl30.tfm) = %{tl_version}
Provides:       tex(gbkyousl31.tfm) = %{tl_version}, tex(gbkyousl32.tfm) = %{tl_version}
Provides:       tex(gbkyousl33.tfm) = %{tl_version}, tex(gbkyousl34.tfm) = %{tl_version}
Provides:       tex(gbkyousl35.tfm) = %{tl_version}, tex(gbkyousl36.tfm) = %{tl_version}
Provides:       tex(gbkyousl37.tfm) = %{tl_version}, tex(gbkyousl38.tfm) = %{tl_version}
Provides:       tex(gbkyousl39.tfm) = %{tl_version}, tex(gbkyousl40.tfm) = %{tl_version}
Provides:       tex(gbkyousl41.tfm) = %{tl_version}, tex(gbkyousl42.tfm) = %{tl_version}
Provides:       tex(gbkyousl43.tfm) = %{tl_version}, tex(gbkyousl44.tfm) = %{tl_version}
Provides:       tex(gbkyousl45.tfm) = %{tl_version}, tex(gbkyousl46.tfm) = %{tl_version}
Provides:       tex(gbkyousl47.tfm) = %{tl_version}, tex(gbkyousl48.tfm) = %{tl_version}
Provides:       tex(gbkyousl49.tfm) = %{tl_version}, tex(gbkyousl50.tfm) = %{tl_version}
Provides:       tex(gbkyousl51.tfm) = %{tl_version}, tex(gbkyousl52.tfm) = %{tl_version}
Provides:       tex(gbkyousl53.tfm) = %{tl_version}, tex(gbkyousl54.tfm) = %{tl_version}
Provides:       tex(gbkyousl55.tfm) = %{tl_version}, tex(gbkyousl56.tfm) = %{tl_version}
Provides:       tex(gbkyousl57.tfm) = %{tl_version}, tex(gbkyousl58.tfm) = %{tl_version}
Provides:       tex(gbkyousl59.tfm) = %{tl_version}, tex(gbkyousl60.tfm) = %{tl_version}
Provides:       tex(gbkyousl61.tfm) = %{tl_version}, tex(gbkyousl62.tfm) = %{tl_version}
Provides:       tex(gbkyousl63.tfm) = %{tl_version}, tex(gbkyousl64.tfm) = %{tl_version}
Provides:       tex(gbkyousl65.tfm) = %{tl_version}, tex(gbkyousl66.tfm) = %{tl_version}
Provides:       tex(gbkyousl67.tfm) = %{tl_version}, tex(gbkyousl68.tfm) = %{tl_version}
Provides:       tex(gbkyousl69.tfm) = %{tl_version}, tex(gbkyousl70.tfm) = %{tl_version}
Provides:       tex(gbkyousl71.tfm) = %{tl_version}, tex(gbkyousl72.tfm) = %{tl_version}
Provides:       tex(gbkyousl73.tfm) = %{tl_version}, tex(gbkyousl74.tfm) = %{tl_version}
Provides:       tex(gbkyousl75.tfm) = %{tl_version}, tex(gbkyousl76.tfm) = %{tl_version}
Provides:       tex(gbkyousl77.tfm) = %{tl_version}, tex(gbkyousl78.tfm) = %{tl_version}
Provides:       tex(gbkyousl79.tfm) = %{tl_version}, tex(gbkyousl80.tfm) = %{tl_version}
Provides:       tex(gbkyousl81.tfm) = %{tl_version}, tex(gbkyousl82.tfm) = %{tl_version}
Provides:       tex(gbkyousl83.tfm) = %{tl_version}, tex(gbkyousl84.tfm) = %{tl_version}
Provides:       tex(gbkyousl85.tfm) = %{tl_version}, tex(gbkyousl86.tfm) = %{tl_version}
Provides:       tex(gbkyousl87.tfm) = %{tl_version}, tex(gbkyousl88.tfm) = %{tl_version}
Provides:       tex(gbkyousl89.tfm) = %{tl_version}, tex(gbkyousl90.tfm) = %{tl_version}
Provides:       tex(gbkyousl91.tfm) = %{tl_version}, tex(gbkyousl92.tfm) = %{tl_version}
Provides:       tex(gbkyousl93.tfm) = %{tl_version}, tex(gbkyousl94.tfm) = %{tl_version}
Provides:       tex(unifs00.tfm) = %{tl_version}, tex(unifs01.tfm) = %{tl_version}
Provides:       tex(unifs02.tfm) = %{tl_version}, tex(unifs03.tfm) = %{tl_version}
Provides:       tex(unifs04.tfm) = %{tl_version}, tex(unifs05.tfm) = %{tl_version}
Provides:       tex(unifs06.tfm) = %{tl_version}, tex(unifs07.tfm) = %{tl_version}
Provides:       tex(unifs08.tfm) = %{tl_version}, tex(unifs09.tfm) = %{tl_version}
Provides:       tex(unifs0a.tfm) = %{tl_version}, tex(unifs0b.tfm) = %{tl_version}
Provides:       tex(unifs0c.tfm) = %{tl_version}, tex(unifs0d.tfm) = %{tl_version}
Provides:       tex(unifs0e.tfm) = %{tl_version}, tex(unifs0f.tfm) = %{tl_version}
Provides:       tex(unifs10.tfm) = %{tl_version}, tex(unifs11.tfm) = %{tl_version}
Provides:       tex(unifs12.tfm) = %{tl_version}, tex(unifs13.tfm) = %{tl_version}
Provides:       tex(unifs14.tfm) = %{tl_version}, tex(unifs15.tfm) = %{tl_version}
Provides:       tex(unifs16.tfm) = %{tl_version}, tex(unifs17.tfm) = %{tl_version}
Provides:       tex(unifs18.tfm) = %{tl_version}, tex(unifs19.tfm) = %{tl_version}
Provides:       tex(unifs1a.tfm) = %{tl_version}, tex(unifs1b.tfm) = %{tl_version}
Provides:       tex(unifs1c.tfm) = %{tl_version}, tex(unifs1d.tfm) = %{tl_version}
Provides:       tex(unifs1e.tfm) = %{tl_version}, tex(unifs1f.tfm) = %{tl_version}
Provides:       tex(unifs20.tfm) = %{tl_version}, tex(unifs21.tfm) = %{tl_version}
Provides:       tex(unifs22.tfm) = %{tl_version}, tex(unifs23.tfm) = %{tl_version}
Provides:       tex(unifs24.tfm) = %{tl_version}, tex(unifs25.tfm) = %{tl_version}
Provides:       tex(unifs26.tfm) = %{tl_version}, tex(unifs27.tfm) = %{tl_version}
Provides:       tex(unifs28.tfm) = %{tl_version}, tex(unifs29.tfm) = %{tl_version}
Provides:       tex(unifs2a.tfm) = %{tl_version}, tex(unifs2b.tfm) = %{tl_version}
Provides:       tex(unifs2c.tfm) = %{tl_version}, tex(unifs2d.tfm) = %{tl_version}
Provides:       tex(unifs2e.tfm) = %{tl_version}, tex(unifs2f.tfm) = %{tl_version}
Provides:       tex(unifs30.tfm) = %{tl_version}, tex(unifs31.tfm) = %{tl_version}
Provides:       tex(unifs32.tfm) = %{tl_version}, tex(unifs33.tfm) = %{tl_version}
Provides:       tex(unifs34.tfm) = %{tl_version}, tex(unifs35.tfm) = %{tl_version}
Provides:       tex(unifs36.tfm) = %{tl_version}, tex(unifs37.tfm) = %{tl_version}
Provides:       tex(unifs38.tfm) = %{tl_version}, tex(unifs39.tfm) = %{tl_version}
Provides:       tex(unifs3a.tfm) = %{tl_version}, tex(unifs3b.tfm) = %{tl_version}
Provides:       tex(unifs3c.tfm) = %{tl_version}, tex(unifs3d.tfm) = %{tl_version}
Provides:       tex(unifs3e.tfm) = %{tl_version}, tex(unifs3f.tfm) = %{tl_version}
Provides:       tex(unifs40.tfm) = %{tl_version}, tex(unifs41.tfm) = %{tl_version}
Provides:       tex(unifs42.tfm) = %{tl_version}, tex(unifs43.tfm) = %{tl_version}
Provides:       tex(unifs44.tfm) = %{tl_version}, tex(unifs45.tfm) = %{tl_version}
Provides:       tex(unifs46.tfm) = %{tl_version}, tex(unifs47.tfm) = %{tl_version}
Provides:       tex(unifs48.tfm) = %{tl_version}, tex(unifs49.tfm) = %{tl_version}
Provides:       tex(unifs4a.tfm) = %{tl_version}, tex(unifs4b.tfm) = %{tl_version}
Provides:       tex(unifs4c.tfm) = %{tl_version}, tex(unifs4d.tfm) = %{tl_version}
Provides:       tex(unifs4e.tfm) = %{tl_version}, tex(unifs4f.tfm) = %{tl_version}
Provides:       tex(unifs50.tfm) = %{tl_version}, tex(unifs51.tfm) = %{tl_version}
Provides:       tex(unifs52.tfm) = %{tl_version}, tex(unifs53.tfm) = %{tl_version}
Provides:       tex(unifs54.tfm) = %{tl_version}, tex(unifs55.tfm) = %{tl_version}
Provides:       tex(unifs56.tfm) = %{tl_version}, tex(unifs57.tfm) = %{tl_version}
Provides:       tex(unifs58.tfm) = %{tl_version}, tex(unifs59.tfm) = %{tl_version}
Provides:       tex(unifs5a.tfm) = %{tl_version}, tex(unifs5b.tfm) = %{tl_version}
Provides:       tex(unifs5c.tfm) = %{tl_version}, tex(unifs5d.tfm) = %{tl_version}
Provides:       tex(unifs5e.tfm) = %{tl_version}, tex(unifs5f.tfm) = %{tl_version}
Provides:       tex(unifs60.tfm) = %{tl_version}, tex(unifs61.tfm) = %{tl_version}
Provides:       tex(unifs62.tfm) = %{tl_version}, tex(unifs63.tfm) = %{tl_version}
Provides:       tex(unifs64.tfm) = %{tl_version}, tex(unifs65.tfm) = %{tl_version}
Provides:       tex(unifs66.tfm) = %{tl_version}, tex(unifs67.tfm) = %{tl_version}
Provides:       tex(unifs68.tfm) = %{tl_version}, tex(unifs69.tfm) = %{tl_version}
Provides:       tex(unifs6a.tfm) = %{tl_version}, tex(unifs6b.tfm) = %{tl_version}
Provides:       tex(unifs6c.tfm) = %{tl_version}, tex(unifs6d.tfm) = %{tl_version}
Provides:       tex(unifs6e.tfm) = %{tl_version}, tex(unifs6f.tfm) = %{tl_version}
Provides:       tex(unifs70.tfm) = %{tl_version}, tex(unifs71.tfm) = %{tl_version}
Provides:       tex(unifs72.tfm) = %{tl_version}, tex(unifs73.tfm) = %{tl_version}
Provides:       tex(unifs74.tfm) = %{tl_version}, tex(unifs75.tfm) = %{tl_version}
Provides:       tex(unifs76.tfm) = %{tl_version}, tex(unifs77.tfm) = %{tl_version}
Provides:       tex(unifs78.tfm) = %{tl_version}, tex(unifs79.tfm) = %{tl_version}
Provides:       tex(unifs7a.tfm) = %{tl_version}, tex(unifs7b.tfm) = %{tl_version}
Provides:       tex(unifs7c.tfm) = %{tl_version}, tex(unifs7d.tfm) = %{tl_version}
Provides:       tex(unifs7e.tfm) = %{tl_version}, tex(unifs7f.tfm) = %{tl_version}
Provides:       tex(unifs80.tfm) = %{tl_version}, tex(unifs81.tfm) = %{tl_version}
Provides:       tex(unifs82.tfm) = %{tl_version}, tex(unifs83.tfm) = %{tl_version}
Provides:       tex(unifs84.tfm) = %{tl_version}, tex(unifs85.tfm) = %{tl_version}
Provides:       tex(unifs86.tfm) = %{tl_version}, tex(unifs87.tfm) = %{tl_version}
Provides:       tex(unifs88.tfm) = %{tl_version}, tex(unifs89.tfm) = %{tl_version}
Provides:       tex(unifs8a.tfm) = %{tl_version}, tex(unifs8b.tfm) = %{tl_version}
Provides:       tex(unifs8c.tfm) = %{tl_version}, tex(unifs8d.tfm) = %{tl_version}
Provides:       tex(unifs8e.tfm) = %{tl_version}, tex(unifs8f.tfm) = %{tl_version}
Provides:       tex(unifs90.tfm) = %{tl_version}, tex(unifs91.tfm) = %{tl_version}
Provides:       tex(unifs92.tfm) = %{tl_version}, tex(unifs93.tfm) = %{tl_version}
Provides:       tex(unifs94.tfm) = %{tl_version}, tex(unifs95.tfm) = %{tl_version}
Provides:       tex(unifs96.tfm) = %{tl_version}, tex(unifs97.tfm) = %{tl_version}
Provides:       tex(unifs98.tfm) = %{tl_version}, tex(unifs99.tfm) = %{tl_version}
Provides:       tex(unifs9a.tfm) = %{tl_version}, tex(unifs9b.tfm) = %{tl_version}
Provides:       tex(unifs9c.tfm) = %{tl_version}, tex(unifs9d.tfm) = %{tl_version}
Provides:       tex(unifs9e.tfm) = %{tl_version}, tex(unifs9f.tfm) = %{tl_version}
Provides:       tex(unifsa0.tfm) = %{tl_version}, tex(unifsa1.tfm) = %{tl_version}
Provides:       tex(unifsa2.tfm) = %{tl_version}, tex(unifsa3.tfm) = %{tl_version}
Provides:       tex(unifsa4.tfm) = %{tl_version}, tex(unifsa5.tfm) = %{tl_version}
Provides:       tex(unifsa6.tfm) = %{tl_version}, tex(unifsa7.tfm) = %{tl_version}
Provides:       tex(unifsa8.tfm) = %{tl_version}, tex(unifsa9.tfm) = %{tl_version}
Provides:       tex(unifsaa.tfm) = %{tl_version}, tex(unifsab.tfm) = %{tl_version}
Provides:       tex(unifsac.tfm) = %{tl_version}, tex(unifsad.tfm) = %{tl_version}
Provides:       tex(unifsae.tfm) = %{tl_version}, tex(unifsaf.tfm) = %{tl_version}
Provides:       tex(unifsb0.tfm) = %{tl_version}, tex(unifsb1.tfm) = %{tl_version}
Provides:       tex(unifsb2.tfm) = %{tl_version}, tex(unifsb3.tfm) = %{tl_version}
Provides:       tex(unifsb4.tfm) = %{tl_version}, tex(unifsb5.tfm) = %{tl_version}
Provides:       tex(unifsb6.tfm) = %{tl_version}, tex(unifsb7.tfm) = %{tl_version}
Provides:       tex(unifsb8.tfm) = %{tl_version}, tex(unifsb9.tfm) = %{tl_version}
Provides:       tex(unifsba.tfm) = %{tl_version}, tex(unifsbb.tfm) = %{tl_version}
Provides:       tex(unifsbc.tfm) = %{tl_version}, tex(unifsbd.tfm) = %{tl_version}
Provides:       tex(unifsbe.tfm) = %{tl_version}, tex(unifsbf.tfm) = %{tl_version}
Provides:       tex(unifsc0.tfm) = %{tl_version}, tex(unifsc1.tfm) = %{tl_version}
Provides:       tex(unifsc2.tfm) = %{tl_version}, tex(unifsc3.tfm) = %{tl_version}
Provides:       tex(unifsc4.tfm) = %{tl_version}, tex(unifsc5.tfm) = %{tl_version}
Provides:       tex(unifsc6.tfm) = %{tl_version}, tex(unifsc7.tfm) = %{tl_version}
Provides:       tex(unifsc8.tfm) = %{tl_version}, tex(unifsc9.tfm) = %{tl_version}
Provides:       tex(unifsca.tfm) = %{tl_version}, tex(unifscb.tfm) = %{tl_version}
Provides:       tex(unifscc.tfm) = %{tl_version}, tex(unifscd.tfm) = %{tl_version}
Provides:       tex(unifsce.tfm) = %{tl_version}, tex(unifscf.tfm) = %{tl_version}
Provides:       tex(unifsd0.tfm) = %{tl_version}, tex(unifsd1.tfm) = %{tl_version}
Provides:       tex(unifsd2.tfm) = %{tl_version}, tex(unifsd3.tfm) = %{tl_version}
Provides:       tex(unifsd4.tfm) = %{tl_version}, tex(unifsd5.tfm) = %{tl_version}
Provides:       tex(unifsd6.tfm) = %{tl_version}, tex(unifsd7.tfm) = %{tl_version}
Provides:       tex(unifsd8.tfm) = %{tl_version}, tex(unifsd9.tfm) = %{tl_version}
Provides:       tex(unifsda.tfm) = %{tl_version}, tex(unifsdb.tfm) = %{tl_version}
Provides:       tex(unifsdc.tfm) = %{tl_version}, tex(unifsdd.tfm) = %{tl_version}
Provides:       tex(unifsde.tfm) = %{tl_version}, tex(unifsdf.tfm) = %{tl_version}
Provides:       tex(unifse0.tfm) = %{tl_version}, tex(unifse1.tfm) = %{tl_version}
Provides:       tex(unifse2.tfm) = %{tl_version}, tex(unifse3.tfm) = %{tl_version}
Provides:       tex(unifse4.tfm) = %{tl_version}, tex(unifse5.tfm) = %{tl_version}
Provides:       tex(unifse6.tfm) = %{tl_version}, tex(unifse7.tfm) = %{tl_version}
Provides:       tex(unifse8.tfm) = %{tl_version}, tex(unifse9.tfm) = %{tl_version}
Provides:       tex(unifsea.tfm) = %{tl_version}, tex(unifseb.tfm) = %{tl_version}
Provides:       tex(unifsec.tfm) = %{tl_version}, tex(unifsed.tfm) = %{tl_version}
Provides:       tex(unifsee.tfm) = %{tl_version}, tex(unifsef.tfm) = %{tl_version}
Provides:       tex(unifsf0.tfm) = %{tl_version}, tex(unifsf1.tfm) = %{tl_version}
Provides:       tex(unifsf2.tfm) = %{tl_version}, tex(unifsf3.tfm) = %{tl_version}
Provides:       tex(unifsf4.tfm) = %{tl_version}, tex(unifsf5.tfm) = %{tl_version}
Provides:       tex(unifsf6.tfm) = %{tl_version}, tex(unifsf7.tfm) = %{tl_version}
Provides:       tex(unifsf8.tfm) = %{tl_version}, tex(unifsf9.tfm) = %{tl_version}
Provides:       tex(unifsfa.tfm) = %{tl_version}, tex(unifsfb.tfm) = %{tl_version}
Provides:       tex(unifsfc.tfm) = %{tl_version}, tex(unifsfd.tfm) = %{tl_version}
Provides:       tex(unifsfe.tfm) = %{tl_version}, tex(unifsff.tfm) = %{tl_version}
Provides:       tex(unifssl00.tfm) = %{tl_version}, tex(unifssl01.tfm) = %{tl_version}
Provides:       tex(unifssl02.tfm) = %{tl_version}, tex(unifssl03.tfm) = %{tl_version}
Provides:       tex(unifssl04.tfm) = %{tl_version}, tex(unifssl05.tfm) = %{tl_version}
Provides:       tex(unifssl06.tfm) = %{tl_version}, tex(unifssl07.tfm) = %{tl_version}
Provides:       tex(unifssl08.tfm) = %{tl_version}, tex(unifssl09.tfm) = %{tl_version}
Provides:       tex(unifssl0a.tfm) = %{tl_version}, tex(unifssl0b.tfm) = %{tl_version}
Provides:       tex(unifssl0c.tfm) = %{tl_version}, tex(unifssl0d.tfm) = %{tl_version}
Provides:       tex(unifssl0e.tfm) = %{tl_version}, tex(unifssl0f.tfm) = %{tl_version}
Provides:       tex(unifssl10.tfm) = %{tl_version}, tex(unifssl11.tfm) = %{tl_version}
Provides:       tex(unifssl12.tfm) = %{tl_version}, tex(unifssl13.tfm) = %{tl_version}
Provides:       tex(unifssl14.tfm) = %{tl_version}, tex(unifssl15.tfm) = %{tl_version}
Provides:       tex(unifssl16.tfm) = %{tl_version}, tex(unifssl17.tfm) = %{tl_version}
Provides:       tex(unifssl18.tfm) = %{tl_version}, tex(unifssl19.tfm) = %{tl_version}
Provides:       tex(unifssl1a.tfm) = %{tl_version}, tex(unifssl1b.tfm) = %{tl_version}
Provides:       tex(unifssl1c.tfm) = %{tl_version}, tex(unifssl1d.tfm) = %{tl_version}
Provides:       tex(unifssl1e.tfm) = %{tl_version}, tex(unifssl1f.tfm) = %{tl_version}
Provides:       tex(unifssl20.tfm) = %{tl_version}, tex(unifssl21.tfm) = %{tl_version}
Provides:       tex(unifssl22.tfm) = %{tl_version}, tex(unifssl23.tfm) = %{tl_version}
Provides:       tex(unifssl24.tfm) = %{tl_version}, tex(unifssl25.tfm) = %{tl_version}
Provides:       tex(unifssl26.tfm) = %{tl_version}, tex(unifssl27.tfm) = %{tl_version}
Provides:       tex(unifssl28.tfm) = %{tl_version}, tex(unifssl29.tfm) = %{tl_version}
Provides:       tex(unifssl2a.tfm) = %{tl_version}, tex(unifssl2b.tfm) = %{tl_version}
Provides:       tex(unifssl2c.tfm) = %{tl_version}, tex(unifssl2d.tfm) = %{tl_version}
Provides:       tex(unifssl2e.tfm) = %{tl_version}, tex(unifssl2f.tfm) = %{tl_version}
Provides:       tex(unifssl30.tfm) = %{tl_version}, tex(unifssl31.tfm) = %{tl_version}
Provides:       tex(unifssl32.tfm) = %{tl_version}, tex(unifssl33.tfm) = %{tl_version}
Provides:       tex(unifssl34.tfm) = %{tl_version}, tex(unifssl35.tfm) = %{tl_version}
Provides:       tex(unifssl36.tfm) = %{tl_version}, tex(unifssl37.tfm) = %{tl_version}
Provides:       tex(unifssl38.tfm) = %{tl_version}, tex(unifssl39.tfm) = %{tl_version}
Provides:       tex(unifssl3a.tfm) = %{tl_version}, tex(unifssl3b.tfm) = %{tl_version}
Provides:       tex(unifssl3c.tfm) = %{tl_version}, tex(unifssl3d.tfm) = %{tl_version}
Provides:       tex(unifssl3e.tfm) = %{tl_version}, tex(unifssl3f.tfm) = %{tl_version}
Provides:       tex(unifssl40.tfm) = %{tl_version}, tex(unifssl41.tfm) = %{tl_version}
Provides:       tex(unifssl42.tfm) = %{tl_version}, tex(unifssl43.tfm) = %{tl_version}
Provides:       tex(unifssl44.tfm) = %{tl_version}, tex(unifssl45.tfm) = %{tl_version}
Provides:       tex(unifssl46.tfm) = %{tl_version}, tex(unifssl47.tfm) = %{tl_version}
Provides:       tex(unifssl48.tfm) = %{tl_version}, tex(unifssl49.tfm) = %{tl_version}
Provides:       tex(unifssl4a.tfm) = %{tl_version}, tex(unifssl4b.tfm) = %{tl_version}
Provides:       tex(unifssl4c.tfm) = %{tl_version}, tex(unifssl4d.tfm) = %{tl_version}
Provides:       tex(unifssl4e.tfm) = %{tl_version}, tex(unifssl4f.tfm) = %{tl_version}
Provides:       tex(unifssl50.tfm) = %{tl_version}, tex(unifssl51.tfm) = %{tl_version}
Provides:       tex(unifssl52.tfm) = %{tl_version}, tex(unifssl53.tfm) = %{tl_version}
Provides:       tex(unifssl54.tfm) = %{tl_version}, tex(unifssl55.tfm) = %{tl_version}
Provides:       tex(unifssl56.tfm) = %{tl_version}, tex(unifssl57.tfm) = %{tl_version}
Provides:       tex(unifssl58.tfm) = %{tl_version}, tex(unifssl59.tfm) = %{tl_version}
Provides:       tex(unifssl5a.tfm) = %{tl_version}, tex(unifssl5b.tfm) = %{tl_version}
Provides:       tex(unifssl5c.tfm) = %{tl_version}, tex(unifssl5d.tfm) = %{tl_version}
Provides:       tex(unifssl5e.tfm) = %{tl_version}, tex(unifssl5f.tfm) = %{tl_version}
Provides:       tex(unifssl60.tfm) = %{tl_version}, tex(unifssl61.tfm) = %{tl_version}
Provides:       tex(unifssl62.tfm) = %{tl_version}, tex(unifssl63.tfm) = %{tl_version}
Provides:       tex(unifssl64.tfm) = %{tl_version}, tex(unifssl65.tfm) = %{tl_version}
Provides:       tex(unifssl66.tfm) = %{tl_version}, tex(unifssl67.tfm) = %{tl_version}
Provides:       tex(unifssl68.tfm) = %{tl_version}, tex(unifssl69.tfm) = %{tl_version}
Provides:       tex(unifssl6a.tfm) = %{tl_version}, tex(unifssl6b.tfm) = %{tl_version}
Provides:       tex(unifssl6c.tfm) = %{tl_version}, tex(unifssl6d.tfm) = %{tl_version}
Provides:       tex(unifssl6e.tfm) = %{tl_version}, tex(unifssl6f.tfm) = %{tl_version}
Provides:       tex(unifssl70.tfm) = %{tl_version}, tex(unifssl71.tfm) = %{tl_version}
Provides:       tex(unifssl72.tfm) = %{tl_version}, tex(unifssl73.tfm) = %{tl_version}
Provides:       tex(unifssl74.tfm) = %{tl_version}, tex(unifssl75.tfm) = %{tl_version}
Provides:       tex(unifssl76.tfm) = %{tl_version}, tex(unifssl77.tfm) = %{tl_version}
Provides:       tex(unifssl78.tfm) = %{tl_version}, tex(unifssl79.tfm) = %{tl_version}
Provides:       tex(unifssl7a.tfm) = %{tl_version}, tex(unifssl7b.tfm) = %{tl_version}
Provides:       tex(unifssl7c.tfm) = %{tl_version}, tex(unifssl7d.tfm) = %{tl_version}
Provides:       tex(unifssl7e.tfm) = %{tl_version}, tex(unifssl7f.tfm) = %{tl_version}
Provides:       tex(unifssl80.tfm) = %{tl_version}, tex(unifssl81.tfm) = %{tl_version}
Provides:       tex(unifssl82.tfm) = %{tl_version}, tex(unifssl83.tfm) = %{tl_version}
Provides:       tex(unifssl84.tfm) = %{tl_version}, tex(unifssl85.tfm) = %{tl_version}
Provides:       tex(unifssl86.tfm) = %{tl_version}, tex(unifssl87.tfm) = %{tl_version}
Provides:       tex(unifssl88.tfm) = %{tl_version}, tex(unifssl89.tfm) = %{tl_version}
Provides:       tex(unifssl8a.tfm) = %{tl_version}, tex(unifssl8b.tfm) = %{tl_version}
Provides:       tex(unifssl8c.tfm) = %{tl_version}, tex(unifssl8d.tfm) = %{tl_version}
Provides:       tex(unifssl8e.tfm) = %{tl_version}, tex(unifssl8f.tfm) = %{tl_version}
Provides:       tex(unifssl90.tfm) = %{tl_version}, tex(unifssl91.tfm) = %{tl_version}
Provides:       tex(unifssl92.tfm) = %{tl_version}, tex(unifssl93.tfm) = %{tl_version}
Provides:       tex(unifssl94.tfm) = %{tl_version}, tex(unifssl95.tfm) = %{tl_version}
Provides:       tex(unifssl96.tfm) = %{tl_version}, tex(unifssl97.tfm) = %{tl_version}
Provides:       tex(unifssl98.tfm) = %{tl_version}, tex(unifssl99.tfm) = %{tl_version}
Provides:       tex(unifssl9a.tfm) = %{tl_version}, tex(unifssl9b.tfm) = %{tl_version}
Provides:       tex(unifssl9c.tfm) = %{tl_version}, tex(unifssl9d.tfm) = %{tl_version}
Provides:       tex(unifssl9e.tfm) = %{tl_version}, tex(unifssl9f.tfm) = %{tl_version}
Provides:       tex(unifssla0.tfm) = %{tl_version}, tex(unifssla1.tfm) = %{tl_version}
Provides:       tex(unifssla2.tfm) = %{tl_version}, tex(unifssla3.tfm) = %{tl_version}
Provides:       tex(unifssla4.tfm) = %{tl_version}, tex(unifssla5.tfm) = %{tl_version}
Provides:       tex(unifssla6.tfm) = %{tl_version}, tex(unifssla7.tfm) = %{tl_version}
Provides:       tex(unifssla8.tfm) = %{tl_version}, tex(unifssla9.tfm) = %{tl_version}
Provides:       tex(unifsslaa.tfm) = %{tl_version}, tex(unifsslab.tfm) = %{tl_version}
Provides:       tex(unifsslac.tfm) = %{tl_version}, tex(unifsslad.tfm) = %{tl_version}
Provides:       tex(unifsslae.tfm) = %{tl_version}, tex(unifsslaf.tfm) = %{tl_version}
Provides:       tex(unifsslb0.tfm) = %{tl_version}, tex(unifsslb1.tfm) = %{tl_version}
Provides:       tex(unifsslb2.tfm) = %{tl_version}, tex(unifsslb3.tfm) = %{tl_version}
Provides:       tex(unifsslb4.tfm) = %{tl_version}, tex(unifsslb5.tfm) = %{tl_version}
Provides:       tex(unifsslb6.tfm) = %{tl_version}, tex(unifsslb7.tfm) = %{tl_version}
Provides:       tex(unifsslb8.tfm) = %{tl_version}, tex(unifsslb9.tfm) = %{tl_version}
Provides:       tex(unifsslba.tfm) = %{tl_version}, tex(unifsslbb.tfm) = %{tl_version}
Provides:       tex(unifsslbc.tfm) = %{tl_version}, tex(unifsslbd.tfm) = %{tl_version}
Provides:       tex(unifsslbe.tfm) = %{tl_version}, tex(unifsslbf.tfm) = %{tl_version}
Provides:       tex(unifsslc0.tfm) = %{tl_version}, tex(unifsslc1.tfm) = %{tl_version}
Provides:       tex(unifsslc2.tfm) = %{tl_version}, tex(unifsslc3.tfm) = %{tl_version}
Provides:       tex(unifsslc4.tfm) = %{tl_version}, tex(unifsslc5.tfm) = %{tl_version}
Provides:       tex(unifsslc6.tfm) = %{tl_version}, tex(unifsslc7.tfm) = %{tl_version}
Provides:       tex(unifsslc8.tfm) = %{tl_version}, tex(unifsslc9.tfm) = %{tl_version}
Provides:       tex(unifsslca.tfm) = %{tl_version}, tex(unifsslcb.tfm) = %{tl_version}
Provides:       tex(unifsslcc.tfm) = %{tl_version}, tex(unifsslcd.tfm) = %{tl_version}
Provides:       tex(unifsslce.tfm) = %{tl_version}, tex(unifsslcf.tfm) = %{tl_version}
Provides:       tex(unifssld0.tfm) = %{tl_version}, tex(unifssld1.tfm) = %{tl_version}
Provides:       tex(unifssld2.tfm) = %{tl_version}, tex(unifssld3.tfm) = %{tl_version}
Provides:       tex(unifssld4.tfm) = %{tl_version}, tex(unifssld5.tfm) = %{tl_version}
Provides:       tex(unifssld6.tfm) = %{tl_version}, tex(unifssld7.tfm) = %{tl_version}
Provides:       tex(unifssld8.tfm) = %{tl_version}, tex(unifssld9.tfm) = %{tl_version}
Provides:       tex(unifsslda.tfm) = %{tl_version}, tex(unifssldb.tfm) = %{tl_version}
Provides:       tex(unifssldc.tfm) = %{tl_version}, tex(unifssldd.tfm) = %{tl_version}
Provides:       tex(unifsslde.tfm) = %{tl_version}, tex(unifssldf.tfm) = %{tl_version}
Provides:       tex(unifssle0.tfm) = %{tl_version}, tex(unifssle1.tfm) = %{tl_version}
Provides:       tex(unifssle2.tfm) = %{tl_version}, tex(unifssle3.tfm) = %{tl_version}
Provides:       tex(unifssle4.tfm) = %{tl_version}, tex(unifssle5.tfm) = %{tl_version}
Provides:       tex(unifssle6.tfm) = %{tl_version}, tex(unifssle7.tfm) = %{tl_version}
Provides:       tex(unifssle8.tfm) = %{tl_version}, tex(unifssle9.tfm) = %{tl_version}
Provides:       tex(unifsslea.tfm) = %{tl_version}, tex(unifssleb.tfm) = %{tl_version}
Provides:       tex(unifsslec.tfm) = %{tl_version}, tex(unifssled.tfm) = %{tl_version}
Provides:       tex(unifsslee.tfm) = %{tl_version}, tex(unifsslef.tfm) = %{tl_version}
Provides:       tex(unifsslf0.tfm) = %{tl_version}, tex(unifsslf1.tfm) = %{tl_version}
Provides:       tex(unifsslf2.tfm) = %{tl_version}, tex(unifsslf3.tfm) = %{tl_version}
Provides:       tex(unifsslf4.tfm) = %{tl_version}, tex(unifsslf5.tfm) = %{tl_version}
Provides:       tex(unifsslf6.tfm) = %{tl_version}, tex(unifsslf7.tfm) = %{tl_version}
Provides:       tex(unifsslf8.tfm) = %{tl_version}, tex(unifsslf9.tfm) = %{tl_version}
Provides:       tex(unifsslfa.tfm) = %{tl_version}, tex(unifsslfb.tfm) = %{tl_version}
Provides:       tex(unifsslfc.tfm) = %{tl_version}, tex(unifsslfd.tfm) = %{tl_version}
Provides:       tex(unifsslfe.tfm) = %{tl_version}, tex(unifsslff.tfm) = %{tl_version}
Provides:       tex(unihei00.tfm) = %{tl_version}, tex(unihei01.tfm) = %{tl_version}
Provides:       tex(unihei02.tfm) = %{tl_version}, tex(unihei03.tfm) = %{tl_version}
Provides:       tex(unihei04.tfm) = %{tl_version}, tex(unihei05.tfm) = %{tl_version}
Provides:       tex(unihei06.tfm) = %{tl_version}, tex(unihei07.tfm) = %{tl_version}
Provides:       tex(unihei08.tfm) = %{tl_version}, tex(unihei09.tfm) = %{tl_version}
Provides:       tex(unihei0a.tfm) = %{tl_version}, tex(unihei0b.tfm) = %{tl_version}
Provides:       tex(unihei0c.tfm) = %{tl_version}, tex(unihei0d.tfm) = %{tl_version}
Provides:       tex(unihei0e.tfm) = %{tl_version}, tex(unihei0f.tfm) = %{tl_version}
Provides:       tex(unihei10.tfm) = %{tl_version}, tex(unihei11.tfm) = %{tl_version}
Provides:       tex(unihei12.tfm) = %{tl_version}, tex(unihei13.tfm) = %{tl_version}
Provides:       tex(unihei14.tfm) = %{tl_version}, tex(unihei15.tfm) = %{tl_version}
Provides:       tex(unihei16.tfm) = %{tl_version}, tex(unihei17.tfm) = %{tl_version}
Provides:       tex(unihei18.tfm) = %{tl_version}, tex(unihei19.tfm) = %{tl_version}
Provides:       tex(unihei1a.tfm) = %{tl_version}, tex(unihei1b.tfm) = %{tl_version}
Provides:       tex(unihei1c.tfm) = %{tl_version}, tex(unihei1d.tfm) = %{tl_version}
Provides:       tex(unihei1e.tfm) = %{tl_version}, tex(unihei1f.tfm) = %{tl_version}
Provides:       tex(unihei20.tfm) = %{tl_version}, tex(unihei21.tfm) = %{tl_version}
Provides:       tex(unihei22.tfm) = %{tl_version}, tex(unihei23.tfm) = %{tl_version}
Provides:       tex(unihei24.tfm) = %{tl_version}, tex(unihei25.tfm) = %{tl_version}
Provides:       tex(unihei26.tfm) = %{tl_version}, tex(unihei27.tfm) = %{tl_version}
Provides:       tex(unihei28.tfm) = %{tl_version}, tex(unihei29.tfm) = %{tl_version}
Provides:       tex(unihei2a.tfm) = %{tl_version}, tex(unihei2b.tfm) = %{tl_version}
Provides:       tex(unihei2c.tfm) = %{tl_version}, tex(unihei2d.tfm) = %{tl_version}
Provides:       tex(unihei2e.tfm) = %{tl_version}, tex(unihei2f.tfm) = %{tl_version}
Provides:       tex(unihei30.tfm) = %{tl_version}, tex(unihei31.tfm) = %{tl_version}
Provides:       tex(unihei32.tfm) = %{tl_version}, tex(unihei33.tfm) = %{tl_version}
Provides:       tex(unihei34.tfm) = %{tl_version}, tex(unihei35.tfm) = %{tl_version}
Provides:       tex(unihei36.tfm) = %{tl_version}, tex(unihei37.tfm) = %{tl_version}
Provides:       tex(unihei38.tfm) = %{tl_version}, tex(unihei39.tfm) = %{tl_version}
Provides:       tex(unihei3a.tfm) = %{tl_version}, tex(unihei3b.tfm) = %{tl_version}
Provides:       tex(unihei3c.tfm) = %{tl_version}, tex(unihei3d.tfm) = %{tl_version}
Provides:       tex(unihei3e.tfm) = %{tl_version}, tex(unihei3f.tfm) = %{tl_version}
Provides:       tex(unihei40.tfm) = %{tl_version}, tex(unihei41.tfm) = %{tl_version}
Provides:       tex(unihei42.tfm) = %{tl_version}, tex(unihei43.tfm) = %{tl_version}
Provides:       tex(unihei44.tfm) = %{tl_version}, tex(unihei45.tfm) = %{tl_version}
Provides:       tex(unihei46.tfm) = %{tl_version}, tex(unihei47.tfm) = %{tl_version}
Provides:       tex(unihei48.tfm) = %{tl_version}, tex(unihei49.tfm) = %{tl_version}
Provides:       tex(unihei4a.tfm) = %{tl_version}, tex(unihei4b.tfm) = %{tl_version}
Provides:       tex(unihei4c.tfm) = %{tl_version}, tex(unihei4d.tfm) = %{tl_version}
Provides:       tex(unihei4e.tfm) = %{tl_version}, tex(unihei4f.tfm) = %{tl_version}
Provides:       tex(unihei50.tfm) = %{tl_version}, tex(unihei51.tfm) = %{tl_version}
Provides:       tex(unihei52.tfm) = %{tl_version}, tex(unihei53.tfm) = %{tl_version}
Provides:       tex(unihei54.tfm) = %{tl_version}, tex(unihei55.tfm) = %{tl_version}
Provides:       tex(unihei56.tfm) = %{tl_version}, tex(unihei57.tfm) = %{tl_version}
Provides:       tex(unihei58.tfm) = %{tl_version}, tex(unihei59.tfm) = %{tl_version}
Provides:       tex(unihei5a.tfm) = %{tl_version}, tex(unihei5b.tfm) = %{tl_version}
Provides:       tex(unihei5c.tfm) = %{tl_version}, tex(unihei5d.tfm) = %{tl_version}
Provides:       tex(unihei5e.tfm) = %{tl_version}, tex(unihei5f.tfm) = %{tl_version}
Provides:       tex(unihei60.tfm) = %{tl_version}, tex(unihei61.tfm) = %{tl_version}
Provides:       tex(unihei62.tfm) = %{tl_version}, tex(unihei63.tfm) = %{tl_version}
Provides:       tex(unihei64.tfm) = %{tl_version}, tex(unihei65.tfm) = %{tl_version}
Provides:       tex(unihei66.tfm) = %{tl_version}, tex(unihei67.tfm) = %{tl_version}
Provides:       tex(unihei68.tfm) = %{tl_version}, tex(unihei69.tfm) = %{tl_version}
Provides:       tex(unihei6a.tfm) = %{tl_version}, tex(unihei6b.tfm) = %{tl_version}
Provides:       tex(unihei6c.tfm) = %{tl_version}, tex(unihei6d.tfm) = %{tl_version}
Provides:       tex(unihei6e.tfm) = %{tl_version}, tex(unihei6f.tfm) = %{tl_version}
Provides:       tex(unihei70.tfm) = %{tl_version}, tex(unihei71.tfm) = %{tl_version}
Provides:       tex(unihei72.tfm) = %{tl_version}, tex(unihei73.tfm) = %{tl_version}
Provides:       tex(unihei74.tfm) = %{tl_version}, tex(unihei75.tfm) = %{tl_version}
Provides:       tex(unihei76.tfm) = %{tl_version}, tex(unihei77.tfm) = %{tl_version}
Provides:       tex(unihei78.tfm) = %{tl_version}, tex(unihei79.tfm) = %{tl_version}
Provides:       tex(unihei7a.tfm) = %{tl_version}, tex(unihei7b.tfm) = %{tl_version}
Provides:       tex(unihei7c.tfm) = %{tl_version}, tex(unihei7d.tfm) = %{tl_version}
Provides:       tex(unihei7e.tfm) = %{tl_version}, tex(unihei7f.tfm) = %{tl_version}
Provides:       tex(unihei80.tfm) = %{tl_version}, tex(unihei81.tfm) = %{tl_version}
Provides:       tex(unihei82.tfm) = %{tl_version}, tex(unihei83.tfm) = %{tl_version}
Provides:       tex(unihei84.tfm) = %{tl_version}, tex(unihei85.tfm) = %{tl_version}
Provides:       tex(unihei86.tfm) = %{tl_version}, tex(unihei87.tfm) = %{tl_version}
Provides:       tex(unihei88.tfm) = %{tl_version}, tex(unihei89.tfm) = %{tl_version}
Provides:       tex(unihei8a.tfm) = %{tl_version}, tex(unihei8b.tfm) = %{tl_version}
Provides:       tex(unihei8c.tfm) = %{tl_version}, tex(unihei8d.tfm) = %{tl_version}
Provides:       tex(unihei8e.tfm) = %{tl_version}, tex(unihei8f.tfm) = %{tl_version}
Provides:       tex(unihei90.tfm) = %{tl_version}, tex(unihei91.tfm) = %{tl_version}
Provides:       tex(unihei92.tfm) = %{tl_version}, tex(unihei93.tfm) = %{tl_version}
Provides:       tex(unihei94.tfm) = %{tl_version}, tex(unihei95.tfm) = %{tl_version}
Provides:       tex(unihei96.tfm) = %{tl_version}, tex(unihei97.tfm) = %{tl_version}
Provides:       tex(unihei98.tfm) = %{tl_version}, tex(unihei99.tfm) = %{tl_version}
Provides:       tex(unihei9a.tfm) = %{tl_version}, tex(unihei9b.tfm) = %{tl_version}
Provides:       tex(unihei9c.tfm) = %{tl_version}, tex(unihei9d.tfm) = %{tl_version}
Provides:       tex(unihei9e.tfm) = %{tl_version}, tex(unihei9f.tfm) = %{tl_version}
Provides:       tex(uniheia0.tfm) = %{tl_version}, tex(uniheia1.tfm) = %{tl_version}
Provides:       tex(uniheia2.tfm) = %{tl_version}, tex(uniheia3.tfm) = %{tl_version}
Provides:       tex(uniheia4.tfm) = %{tl_version}, tex(uniheia5.tfm) = %{tl_version}
Provides:       tex(uniheia6.tfm) = %{tl_version}, tex(uniheia7.tfm) = %{tl_version}
Provides:       tex(uniheia8.tfm) = %{tl_version}, tex(uniheia9.tfm) = %{tl_version}
Provides:       tex(uniheiaa.tfm) = %{tl_version}, tex(uniheiab.tfm) = %{tl_version}
Provides:       tex(uniheiac.tfm) = %{tl_version}, tex(uniheiad.tfm) = %{tl_version}
Provides:       tex(uniheiae.tfm) = %{tl_version}, tex(uniheiaf.tfm) = %{tl_version}
Provides:       tex(uniheib0.tfm) = %{tl_version}, tex(uniheib1.tfm) = %{tl_version}
Provides:       tex(uniheib2.tfm) = %{tl_version}, tex(uniheib3.tfm) = %{tl_version}
Provides:       tex(uniheib4.tfm) = %{tl_version}, tex(uniheib5.tfm) = %{tl_version}
Provides:       tex(uniheib6.tfm) = %{tl_version}, tex(uniheib7.tfm) = %{tl_version}
Provides:       tex(uniheib8.tfm) = %{tl_version}, tex(uniheib9.tfm) = %{tl_version}
Provides:       tex(uniheiba.tfm) = %{tl_version}, tex(uniheibb.tfm) = %{tl_version}
Provides:       tex(uniheibc.tfm) = %{tl_version}, tex(uniheibd.tfm) = %{tl_version}
Provides:       tex(uniheibe.tfm) = %{tl_version}, tex(uniheibf.tfm) = %{tl_version}
Provides:       tex(uniheic0.tfm) = %{tl_version}, tex(uniheic1.tfm) = %{tl_version}
Provides:       tex(uniheic2.tfm) = %{tl_version}, tex(uniheic3.tfm) = %{tl_version}
Provides:       tex(uniheic4.tfm) = %{tl_version}, tex(uniheic5.tfm) = %{tl_version}
Provides:       tex(uniheic6.tfm) = %{tl_version}, tex(uniheic7.tfm) = %{tl_version}
Provides:       tex(uniheic8.tfm) = %{tl_version}, tex(uniheic9.tfm) = %{tl_version}
Provides:       tex(uniheica.tfm) = %{tl_version}, tex(uniheicb.tfm) = %{tl_version}
Provides:       tex(uniheicc.tfm) = %{tl_version}, tex(uniheicd.tfm) = %{tl_version}
Provides:       tex(uniheice.tfm) = %{tl_version}, tex(uniheicf.tfm) = %{tl_version}
Provides:       tex(uniheid0.tfm) = %{tl_version}, tex(uniheid1.tfm) = %{tl_version}
Provides:       tex(uniheid2.tfm) = %{tl_version}, tex(uniheid3.tfm) = %{tl_version}
Provides:       tex(uniheid4.tfm) = %{tl_version}, tex(uniheid5.tfm) = %{tl_version}
Provides:       tex(uniheid6.tfm) = %{tl_version}, tex(uniheid7.tfm) = %{tl_version}
Provides:       tex(uniheid8.tfm) = %{tl_version}, tex(uniheid9.tfm) = %{tl_version}
Provides:       tex(uniheida.tfm) = %{tl_version}, tex(uniheidb.tfm) = %{tl_version}
Provides:       tex(uniheidc.tfm) = %{tl_version}, tex(uniheidd.tfm) = %{tl_version}
Provides:       tex(uniheide.tfm) = %{tl_version}, tex(uniheidf.tfm) = %{tl_version}
Provides:       tex(uniheie0.tfm) = %{tl_version}, tex(uniheie1.tfm) = %{tl_version}
Provides:       tex(uniheie2.tfm) = %{tl_version}, tex(uniheie3.tfm) = %{tl_version}
Provides:       tex(uniheie4.tfm) = %{tl_version}, tex(uniheie5.tfm) = %{tl_version}
Provides:       tex(uniheie6.tfm) = %{tl_version}, tex(uniheie7.tfm) = %{tl_version}
Provides:       tex(uniheie8.tfm) = %{tl_version}, tex(uniheie9.tfm) = %{tl_version}
Provides:       tex(uniheiea.tfm) = %{tl_version}, tex(uniheieb.tfm) = %{tl_version}
Provides:       tex(uniheiec.tfm) = %{tl_version}, tex(uniheied.tfm) = %{tl_version}
Provides:       tex(uniheiee.tfm) = %{tl_version}, tex(uniheief.tfm) = %{tl_version}
Provides:       tex(uniheif0.tfm) = %{tl_version}, tex(uniheif1.tfm) = %{tl_version}
Provides:       tex(uniheif2.tfm) = %{tl_version}, tex(uniheif3.tfm) = %{tl_version}
Provides:       tex(uniheif4.tfm) = %{tl_version}, tex(uniheif5.tfm) = %{tl_version}
Provides:       tex(uniheif6.tfm) = %{tl_version}, tex(uniheif7.tfm) = %{tl_version}
Provides:       tex(uniheif8.tfm) = %{tl_version}, tex(uniheif9.tfm) = %{tl_version}
Provides:       tex(uniheifa.tfm) = %{tl_version}, tex(uniheifb.tfm) = %{tl_version}
Provides:       tex(uniheifc.tfm) = %{tl_version}, tex(uniheifd.tfm) = %{tl_version}
Provides:       tex(uniheife.tfm) = %{tl_version}, tex(uniheiff.tfm) = %{tl_version}
Provides:       tex(uniheisl00.tfm) = %{tl_version}, tex(uniheisl01.tfm) = %{tl_version}
Provides:       tex(uniheisl02.tfm) = %{tl_version}, tex(uniheisl03.tfm) = %{tl_version}
Provides:       tex(uniheisl04.tfm) = %{tl_version}, tex(uniheisl05.tfm) = %{tl_version}
Provides:       tex(uniheisl06.tfm) = %{tl_version}, tex(uniheisl07.tfm) = %{tl_version}
Provides:       tex(uniheisl08.tfm) = %{tl_version}, tex(uniheisl09.tfm) = %{tl_version}
Provides:       tex(uniheisl0a.tfm) = %{tl_version}, tex(uniheisl0b.tfm) = %{tl_version}
Provides:       tex(uniheisl0c.tfm) = %{tl_version}, tex(uniheisl0d.tfm) = %{tl_version}
Provides:       tex(uniheisl0e.tfm) = %{tl_version}, tex(uniheisl0f.tfm) = %{tl_version}
Provides:       tex(uniheisl10.tfm) = %{tl_version}, tex(uniheisl11.tfm) = %{tl_version}
Provides:       tex(uniheisl12.tfm) = %{tl_version}, tex(uniheisl13.tfm) = %{tl_version}
Provides:       tex(uniheisl14.tfm) = %{tl_version}, tex(uniheisl15.tfm) = %{tl_version}
Provides:       tex(uniheisl16.tfm) = %{tl_version}, tex(uniheisl17.tfm) = %{tl_version}
Provides:       tex(uniheisl18.tfm) = %{tl_version}, tex(uniheisl19.tfm) = %{tl_version}
Provides:       tex(uniheisl1a.tfm) = %{tl_version}, tex(uniheisl1b.tfm) = %{tl_version}
Provides:       tex(uniheisl1c.tfm) = %{tl_version}, tex(uniheisl1d.tfm) = %{tl_version}
Provides:       tex(uniheisl1e.tfm) = %{tl_version}, tex(uniheisl1f.tfm) = %{tl_version}
Provides:       tex(uniheisl20.tfm) = %{tl_version}, tex(uniheisl21.tfm) = %{tl_version}
Provides:       tex(uniheisl22.tfm) = %{tl_version}, tex(uniheisl23.tfm) = %{tl_version}
Provides:       tex(uniheisl24.tfm) = %{tl_version}, tex(uniheisl25.tfm) = %{tl_version}
Provides:       tex(uniheisl26.tfm) = %{tl_version}, tex(uniheisl27.tfm) = %{tl_version}
Provides:       tex(uniheisl28.tfm) = %{tl_version}, tex(uniheisl29.tfm) = %{tl_version}
Provides:       tex(uniheisl2a.tfm) = %{tl_version}, tex(uniheisl2b.tfm) = %{tl_version}
Provides:       tex(uniheisl2c.tfm) = %{tl_version}, tex(uniheisl2d.tfm) = %{tl_version}
Provides:       tex(uniheisl2e.tfm) = %{tl_version}, tex(uniheisl2f.tfm) = %{tl_version}
Provides:       tex(uniheisl30.tfm) = %{tl_version}, tex(uniheisl31.tfm) = %{tl_version}
Provides:       tex(uniheisl32.tfm) = %{tl_version}, tex(uniheisl33.tfm) = %{tl_version}
Provides:       tex(uniheisl34.tfm) = %{tl_version}, tex(uniheisl35.tfm) = %{tl_version}
Provides:       tex(uniheisl36.tfm) = %{tl_version}, tex(uniheisl37.tfm) = %{tl_version}
Provides:       tex(uniheisl38.tfm) = %{tl_version}, tex(uniheisl39.tfm) = %{tl_version}
Provides:       tex(uniheisl3a.tfm) = %{tl_version}, tex(uniheisl3b.tfm) = %{tl_version}
Provides:       tex(uniheisl3c.tfm) = %{tl_version}, tex(uniheisl3d.tfm) = %{tl_version}
Provides:       tex(uniheisl3e.tfm) = %{tl_version}, tex(uniheisl3f.tfm) = %{tl_version}
Provides:       tex(uniheisl40.tfm) = %{tl_version}, tex(uniheisl41.tfm) = %{tl_version}
Provides:       tex(uniheisl42.tfm) = %{tl_version}, tex(uniheisl43.tfm) = %{tl_version}
Provides:       tex(uniheisl44.tfm) = %{tl_version}, tex(uniheisl45.tfm) = %{tl_version}
Provides:       tex(uniheisl46.tfm) = %{tl_version}, tex(uniheisl47.tfm) = %{tl_version}
Provides:       tex(uniheisl48.tfm) = %{tl_version}, tex(uniheisl49.tfm) = %{tl_version}
Provides:       tex(uniheisl4a.tfm) = %{tl_version}, tex(uniheisl4b.tfm) = %{tl_version}
Provides:       tex(uniheisl4c.tfm) = %{tl_version}, tex(uniheisl4d.tfm) = %{tl_version}
Provides:       tex(uniheisl4e.tfm) = %{tl_version}, tex(uniheisl4f.tfm) = %{tl_version}
Provides:       tex(uniheisl50.tfm) = %{tl_version}, tex(uniheisl51.tfm) = %{tl_version}
Provides:       tex(uniheisl52.tfm) = %{tl_version}, tex(uniheisl53.tfm) = %{tl_version}
Provides:       tex(uniheisl54.tfm) = %{tl_version}, tex(uniheisl55.tfm) = %{tl_version}
Provides:       tex(uniheisl56.tfm) = %{tl_version}, tex(uniheisl57.tfm) = %{tl_version}
Provides:       tex(uniheisl58.tfm) = %{tl_version}, tex(uniheisl59.tfm) = %{tl_version}
Provides:       tex(uniheisl5a.tfm) = %{tl_version}, tex(uniheisl5b.tfm) = %{tl_version}
Provides:       tex(uniheisl5c.tfm) = %{tl_version}, tex(uniheisl5d.tfm) = %{tl_version}
Provides:       tex(uniheisl5e.tfm) = %{tl_version}, tex(uniheisl5f.tfm) = %{tl_version}
Provides:       tex(uniheisl60.tfm) = %{tl_version}, tex(uniheisl61.tfm) = %{tl_version}
Provides:       tex(uniheisl62.tfm) = %{tl_version}, tex(uniheisl63.tfm) = %{tl_version}
Provides:       tex(uniheisl64.tfm) = %{tl_version}, tex(uniheisl65.tfm) = %{tl_version}
Provides:       tex(uniheisl66.tfm) = %{tl_version}, tex(uniheisl67.tfm) = %{tl_version}
Provides:       tex(uniheisl68.tfm) = %{tl_version}, tex(uniheisl69.tfm) = %{tl_version}
Provides:       tex(uniheisl6a.tfm) = %{tl_version}, tex(uniheisl6b.tfm) = %{tl_version}
Provides:       tex(uniheisl6c.tfm) = %{tl_version}, tex(uniheisl6d.tfm) = %{tl_version}
Provides:       tex(uniheisl6e.tfm) = %{tl_version}, tex(uniheisl6f.tfm) = %{tl_version}
Provides:       tex(uniheisl70.tfm) = %{tl_version}, tex(uniheisl71.tfm) = %{tl_version}
Provides:       tex(uniheisl72.tfm) = %{tl_version}, tex(uniheisl73.tfm) = %{tl_version}
Provides:       tex(uniheisl74.tfm) = %{tl_version}, tex(uniheisl75.tfm) = %{tl_version}
Provides:       tex(uniheisl76.tfm) = %{tl_version}, tex(uniheisl77.tfm) = %{tl_version}
Provides:       tex(uniheisl78.tfm) = %{tl_version}, tex(uniheisl79.tfm) = %{tl_version}
Provides:       tex(uniheisl7a.tfm) = %{tl_version}, tex(uniheisl7b.tfm) = %{tl_version}
Provides:       tex(uniheisl7c.tfm) = %{tl_version}, tex(uniheisl7d.tfm) = %{tl_version}
Provides:       tex(uniheisl7e.tfm) = %{tl_version}, tex(uniheisl7f.tfm) = %{tl_version}
Provides:       tex(uniheisl80.tfm) = %{tl_version}, tex(uniheisl81.tfm) = %{tl_version}
Provides:       tex(uniheisl82.tfm) = %{tl_version}, tex(uniheisl83.tfm) = %{tl_version}
Provides:       tex(uniheisl84.tfm) = %{tl_version}, tex(uniheisl85.tfm) = %{tl_version}
Provides:       tex(uniheisl86.tfm) = %{tl_version}, tex(uniheisl87.tfm) = %{tl_version}
Provides:       tex(uniheisl88.tfm) = %{tl_version}, tex(uniheisl89.tfm) = %{tl_version}
Provides:       tex(uniheisl8a.tfm) = %{tl_version}, tex(uniheisl8b.tfm) = %{tl_version}
Provides:       tex(uniheisl8c.tfm) = %{tl_version}, tex(uniheisl8d.tfm) = %{tl_version}
Provides:       tex(uniheisl8e.tfm) = %{tl_version}, tex(uniheisl8f.tfm) = %{tl_version}
Provides:       tex(uniheisl90.tfm) = %{tl_version}, tex(uniheisl91.tfm) = %{tl_version}
Provides:       tex(uniheisl92.tfm) = %{tl_version}, tex(uniheisl93.tfm) = %{tl_version}
Provides:       tex(uniheisl94.tfm) = %{tl_version}, tex(uniheisl95.tfm) = %{tl_version}
Provides:       tex(uniheisl96.tfm) = %{tl_version}, tex(uniheisl97.tfm) = %{tl_version}
Provides:       tex(uniheisl98.tfm) = %{tl_version}, tex(uniheisl99.tfm) = %{tl_version}
Provides:       tex(uniheisl9a.tfm) = %{tl_version}, tex(uniheisl9b.tfm) = %{tl_version}
Provides:       tex(uniheisl9c.tfm) = %{tl_version}, tex(uniheisl9d.tfm) = %{tl_version}
Provides:       tex(uniheisl9e.tfm) = %{tl_version}, tex(uniheisl9f.tfm) = %{tl_version}
Provides:       tex(uniheisla0.tfm) = %{tl_version}, tex(uniheisla1.tfm) = %{tl_version}
Provides:       tex(uniheisla2.tfm) = %{tl_version}, tex(uniheisla3.tfm) = %{tl_version}
Provides:       tex(uniheisla4.tfm) = %{tl_version}, tex(uniheisla5.tfm) = %{tl_version}
Provides:       tex(uniheisla6.tfm) = %{tl_version}, tex(uniheisla7.tfm) = %{tl_version}
Provides:       tex(uniheisla8.tfm) = %{tl_version}, tex(uniheisla9.tfm) = %{tl_version}
Provides:       tex(uniheislaa.tfm) = %{tl_version}, tex(uniheislab.tfm) = %{tl_version}
Provides:       tex(uniheislac.tfm) = %{tl_version}, tex(uniheislad.tfm) = %{tl_version}
Provides:       tex(uniheislae.tfm) = %{tl_version}, tex(uniheislaf.tfm) = %{tl_version}
Provides:       tex(uniheislb0.tfm) = %{tl_version}, tex(uniheislb1.tfm) = %{tl_version}
Provides:       tex(uniheislb2.tfm) = %{tl_version}, tex(uniheislb3.tfm) = %{tl_version}
Provides:       tex(uniheislb4.tfm) = %{tl_version}, tex(uniheislb5.tfm) = %{tl_version}
Provides:       tex(uniheislb6.tfm) = %{tl_version}, tex(uniheislb7.tfm) = %{tl_version}
Provides:       tex(uniheislb8.tfm) = %{tl_version}, tex(uniheislb9.tfm) = %{tl_version}
Provides:       tex(uniheislba.tfm) = %{tl_version}, tex(uniheislbb.tfm) = %{tl_version}
Provides:       tex(uniheislbc.tfm) = %{tl_version}, tex(uniheislbd.tfm) = %{tl_version}
Provides:       tex(uniheislbe.tfm) = %{tl_version}, tex(uniheislbf.tfm) = %{tl_version}
Provides:       tex(uniheislc0.tfm) = %{tl_version}, tex(uniheislc1.tfm) = %{tl_version}
Provides:       tex(uniheislc2.tfm) = %{tl_version}, tex(uniheislc3.tfm) = %{tl_version}
Provides:       tex(uniheislc4.tfm) = %{tl_version}, tex(uniheislc5.tfm) = %{tl_version}
Provides:       tex(uniheislc6.tfm) = %{tl_version}, tex(uniheislc7.tfm) = %{tl_version}
Provides:       tex(uniheislc8.tfm) = %{tl_version}, tex(uniheislc9.tfm) = %{tl_version}
Provides:       tex(uniheislca.tfm) = %{tl_version}, tex(uniheislcb.tfm) = %{tl_version}
Provides:       tex(uniheislcc.tfm) = %{tl_version}, tex(uniheislcd.tfm) = %{tl_version}
Provides:       tex(uniheislce.tfm) = %{tl_version}, tex(uniheislcf.tfm) = %{tl_version}
Provides:       tex(uniheisld0.tfm) = %{tl_version}, tex(uniheisld1.tfm) = %{tl_version}
Provides:       tex(uniheisld2.tfm) = %{tl_version}, tex(uniheisld3.tfm) = %{tl_version}
Provides:       tex(uniheisld4.tfm) = %{tl_version}, tex(uniheisld5.tfm) = %{tl_version}
Provides:       tex(uniheisld6.tfm) = %{tl_version}, tex(uniheisld7.tfm) = %{tl_version}
Provides:       tex(uniheisld8.tfm) = %{tl_version}, tex(uniheisld9.tfm) = %{tl_version}
Provides:       tex(uniheislda.tfm) = %{tl_version}, tex(uniheisldb.tfm) = %{tl_version}
Provides:       tex(uniheisldc.tfm) = %{tl_version}, tex(uniheisldd.tfm) = %{tl_version}
Provides:       tex(uniheislde.tfm) = %{tl_version}, tex(uniheisldf.tfm) = %{tl_version}
Provides:       tex(uniheisle0.tfm) = %{tl_version}, tex(uniheisle1.tfm) = %{tl_version}
Provides:       tex(uniheisle2.tfm) = %{tl_version}, tex(uniheisle3.tfm) = %{tl_version}
Provides:       tex(uniheisle4.tfm) = %{tl_version}, tex(uniheisle5.tfm) = %{tl_version}
Provides:       tex(uniheisle6.tfm) = %{tl_version}, tex(uniheisle7.tfm) = %{tl_version}
Provides:       tex(uniheisle8.tfm) = %{tl_version}, tex(uniheisle9.tfm) = %{tl_version}
Provides:       tex(uniheislea.tfm) = %{tl_version}, tex(uniheisleb.tfm) = %{tl_version}
Provides:       tex(uniheislec.tfm) = %{tl_version}, tex(uniheisled.tfm) = %{tl_version}
Provides:       tex(uniheislee.tfm) = %{tl_version}, tex(uniheislef.tfm) = %{tl_version}
Provides:       tex(uniheislf0.tfm) = %{tl_version}, tex(uniheislf1.tfm) = %{tl_version}
Provides:       tex(uniheislf2.tfm) = %{tl_version}, tex(uniheislf3.tfm) = %{tl_version}
Provides:       tex(uniheislf4.tfm) = %{tl_version}, tex(uniheislf5.tfm) = %{tl_version}
Provides:       tex(uniheislf6.tfm) = %{tl_version}, tex(uniheislf7.tfm) = %{tl_version}
Provides:       tex(uniheislf8.tfm) = %{tl_version}, tex(uniheislf9.tfm) = %{tl_version}
Provides:       tex(uniheislfa.tfm) = %{tl_version}, tex(uniheislfb.tfm) = %{tl_version}
Provides:       tex(uniheislfc.tfm) = %{tl_version}, tex(uniheislfd.tfm) = %{tl_version}
Provides:       tex(uniheislfe.tfm) = %{tl_version}, tex(uniheislff.tfm) = %{tl_version}
Provides:       tex(unikai00.tfm) = %{tl_version}, tex(unikai01.tfm) = %{tl_version}
Provides:       tex(unikai02.tfm) = %{tl_version}, tex(unikai03.tfm) = %{tl_version}
Provides:       tex(unikai04.tfm) = %{tl_version}, tex(unikai05.tfm) = %{tl_version}
Provides:       tex(unikai06.tfm) = %{tl_version}, tex(unikai07.tfm) = %{tl_version}
Provides:       tex(unikai08.tfm) = %{tl_version}, tex(unikai09.tfm) = %{tl_version}
Provides:       tex(unikai0a.tfm) = %{tl_version}, tex(unikai0b.tfm) = %{tl_version}
Provides:       tex(unikai0c.tfm) = %{tl_version}, tex(unikai0d.tfm) = %{tl_version}
Provides:       tex(unikai0e.tfm) = %{tl_version}, tex(unikai0f.tfm) = %{tl_version}
Provides:       tex(unikai10.tfm) = %{tl_version}, tex(unikai11.tfm) = %{tl_version}
Provides:       tex(unikai12.tfm) = %{tl_version}, tex(unikai13.tfm) = %{tl_version}
Provides:       tex(unikai14.tfm) = %{tl_version}, tex(unikai15.tfm) = %{tl_version}
Provides:       tex(unikai16.tfm) = %{tl_version}, tex(unikai17.tfm) = %{tl_version}
Provides:       tex(unikai18.tfm) = %{tl_version}, tex(unikai19.tfm) = %{tl_version}
Provides:       tex(unikai1a.tfm) = %{tl_version}, tex(unikai1b.tfm) = %{tl_version}
Provides:       tex(unikai1c.tfm) = %{tl_version}, tex(unikai1d.tfm) = %{tl_version}
Provides:       tex(unikai1e.tfm) = %{tl_version}, tex(unikai1f.tfm) = %{tl_version}
Provides:       tex(unikai20.tfm) = %{tl_version}, tex(unikai21.tfm) = %{tl_version}
Provides:       tex(unikai22.tfm) = %{tl_version}, tex(unikai23.tfm) = %{tl_version}
Provides:       tex(unikai24.tfm) = %{tl_version}, tex(unikai25.tfm) = %{tl_version}
Provides:       tex(unikai26.tfm) = %{tl_version}, tex(unikai27.tfm) = %{tl_version}
Provides:       tex(unikai28.tfm) = %{tl_version}, tex(unikai29.tfm) = %{tl_version}
Provides:       tex(unikai2a.tfm) = %{tl_version}, tex(unikai2b.tfm) = %{tl_version}
Provides:       tex(unikai2c.tfm) = %{tl_version}, tex(unikai2d.tfm) = %{tl_version}
Provides:       tex(unikai2e.tfm) = %{tl_version}, tex(unikai2f.tfm) = %{tl_version}
Provides:       tex(unikai30.tfm) = %{tl_version}, tex(unikai31.tfm) = %{tl_version}
Provides:       tex(unikai32.tfm) = %{tl_version}, tex(unikai33.tfm) = %{tl_version}
Provides:       tex(unikai34.tfm) = %{tl_version}, tex(unikai35.tfm) = %{tl_version}
Provides:       tex(unikai36.tfm) = %{tl_version}, tex(unikai37.tfm) = %{tl_version}
Provides:       tex(unikai38.tfm) = %{tl_version}, tex(unikai39.tfm) = %{tl_version}
Provides:       tex(unikai3a.tfm) = %{tl_version}, tex(unikai3b.tfm) = %{tl_version}
Provides:       tex(unikai3c.tfm) = %{tl_version}, tex(unikai3d.tfm) = %{tl_version}
Provides:       tex(unikai3e.tfm) = %{tl_version}, tex(unikai3f.tfm) = %{tl_version}
Provides:       tex(unikai40.tfm) = %{tl_version}, tex(unikai41.tfm) = %{tl_version}
Provides:       tex(unikai42.tfm) = %{tl_version}, tex(unikai43.tfm) = %{tl_version}
Provides:       tex(unikai44.tfm) = %{tl_version}, tex(unikai45.tfm) = %{tl_version}
Provides:       tex(unikai46.tfm) = %{tl_version}, tex(unikai47.tfm) = %{tl_version}
Provides:       tex(unikai48.tfm) = %{tl_version}, tex(unikai49.tfm) = %{tl_version}
Provides:       tex(unikai4a.tfm) = %{tl_version}, tex(unikai4b.tfm) = %{tl_version}
Provides:       tex(unikai4c.tfm) = %{tl_version}, tex(unikai4d.tfm) = %{tl_version}
Provides:       tex(unikai4e.tfm) = %{tl_version}, tex(unikai4f.tfm) = %{tl_version}
Provides:       tex(unikai50.tfm) = %{tl_version}, tex(unikai51.tfm) = %{tl_version}
Provides:       tex(unikai52.tfm) = %{tl_version}, tex(unikai53.tfm) = %{tl_version}
Provides:       tex(unikai54.tfm) = %{tl_version}, tex(unikai55.tfm) = %{tl_version}
Provides:       tex(unikai56.tfm) = %{tl_version}, tex(unikai57.tfm) = %{tl_version}
Provides:       tex(unikai58.tfm) = %{tl_version}, tex(unikai59.tfm) = %{tl_version}
Provides:       tex(unikai5a.tfm) = %{tl_version}, tex(unikai5b.tfm) = %{tl_version}
Provides:       tex(unikai5c.tfm) = %{tl_version}, tex(unikai5d.tfm) = %{tl_version}
Provides:       tex(unikai5e.tfm) = %{tl_version}, tex(unikai5f.tfm) = %{tl_version}
Provides:       tex(unikai60.tfm) = %{tl_version}, tex(unikai61.tfm) = %{tl_version}
Provides:       tex(unikai62.tfm) = %{tl_version}, tex(unikai63.tfm) = %{tl_version}
Provides:       tex(unikai64.tfm) = %{tl_version}, tex(unikai65.tfm) = %{tl_version}
Provides:       tex(unikai66.tfm) = %{tl_version}, tex(unikai67.tfm) = %{tl_version}
Provides:       tex(unikai68.tfm) = %{tl_version}, tex(unikai69.tfm) = %{tl_version}
Provides:       tex(unikai6a.tfm) = %{tl_version}, tex(unikai6b.tfm) = %{tl_version}
Provides:       tex(unikai6c.tfm) = %{tl_version}, tex(unikai6d.tfm) = %{tl_version}
Provides:       tex(unikai6e.tfm) = %{tl_version}, tex(unikai6f.tfm) = %{tl_version}
Provides:       tex(unikai70.tfm) = %{tl_version}, tex(unikai71.tfm) = %{tl_version}
Provides:       tex(unikai72.tfm) = %{tl_version}, tex(unikai73.tfm) = %{tl_version}
Provides:       tex(unikai74.tfm) = %{tl_version}, tex(unikai75.tfm) = %{tl_version}
Provides:       tex(unikai76.tfm) = %{tl_version}, tex(unikai77.tfm) = %{tl_version}
Provides:       tex(unikai78.tfm) = %{tl_version}, tex(unikai79.tfm) = %{tl_version}
Provides:       tex(unikai7a.tfm) = %{tl_version}, tex(unikai7b.tfm) = %{tl_version}
Provides:       tex(unikai7c.tfm) = %{tl_version}, tex(unikai7d.tfm) = %{tl_version}
Provides:       tex(unikai7e.tfm) = %{tl_version}, tex(unikai7f.tfm) = %{tl_version}
Provides:       tex(unikai80.tfm) = %{tl_version}, tex(unikai81.tfm) = %{tl_version}
Provides:       tex(unikai82.tfm) = %{tl_version}, tex(unikai83.tfm) = %{tl_version}
Provides:       tex(unikai84.tfm) = %{tl_version}, tex(unikai85.tfm) = %{tl_version}
Provides:       tex(unikai86.tfm) = %{tl_version}, tex(unikai87.tfm) = %{tl_version}
Provides:       tex(unikai88.tfm) = %{tl_version}, tex(unikai89.tfm) = %{tl_version}
Provides:       tex(unikai8a.tfm) = %{tl_version}, tex(unikai8b.tfm) = %{tl_version}
Provides:       tex(unikai8c.tfm) = %{tl_version}, tex(unikai8d.tfm) = %{tl_version}
Provides:       tex(unikai8e.tfm) = %{tl_version}, tex(unikai8f.tfm) = %{tl_version}
Provides:       tex(unikai90.tfm) = %{tl_version}, tex(unikai91.tfm) = %{tl_version}
Provides:       tex(unikai92.tfm) = %{tl_version}, tex(unikai93.tfm) = %{tl_version}
Provides:       tex(unikai94.tfm) = %{tl_version}, tex(unikai95.tfm) = %{tl_version}
Provides:       tex(unikai96.tfm) = %{tl_version}, tex(unikai97.tfm) = %{tl_version}
Provides:       tex(unikai98.tfm) = %{tl_version}, tex(unikai99.tfm) = %{tl_version}
Provides:       tex(unikai9a.tfm) = %{tl_version}, tex(unikai9b.tfm) = %{tl_version}
Provides:       tex(unikai9c.tfm) = %{tl_version}, tex(unikai9d.tfm) = %{tl_version}
Provides:       tex(unikai9e.tfm) = %{tl_version}, tex(unikai9f.tfm) = %{tl_version}
Provides:       tex(unikaia0.tfm) = %{tl_version}, tex(unikaia1.tfm) = %{tl_version}
Provides:       tex(unikaia2.tfm) = %{tl_version}, tex(unikaia3.tfm) = %{tl_version}
Provides:       tex(unikaia4.tfm) = %{tl_version}, tex(unikaia5.tfm) = %{tl_version}
Provides:       tex(unikaia6.tfm) = %{tl_version}, tex(unikaia7.tfm) = %{tl_version}
Provides:       tex(unikaia8.tfm) = %{tl_version}, tex(unikaia9.tfm) = %{tl_version}
Provides:       tex(unikaiaa.tfm) = %{tl_version}, tex(unikaiab.tfm) = %{tl_version}
Provides:       tex(unikaiac.tfm) = %{tl_version}, tex(unikaiad.tfm) = %{tl_version}
Provides:       tex(unikaiae.tfm) = %{tl_version}, tex(unikaiaf.tfm) = %{tl_version}
Provides:       tex(unikaib0.tfm) = %{tl_version}, tex(unikaib1.tfm) = %{tl_version}
Provides:       tex(unikaib2.tfm) = %{tl_version}, tex(unikaib3.tfm) = %{tl_version}
Provides:       tex(unikaib4.tfm) = %{tl_version}, tex(unikaib5.tfm) = %{tl_version}
Provides:       tex(unikaib6.tfm) = %{tl_version}, tex(unikaib7.tfm) = %{tl_version}
Provides:       tex(unikaib8.tfm) = %{tl_version}, tex(unikaib9.tfm) = %{tl_version}
Provides:       tex(unikaiba.tfm) = %{tl_version}, tex(unikaibb.tfm) = %{tl_version}
Provides:       tex(unikaibc.tfm) = %{tl_version}, tex(unikaibd.tfm) = %{tl_version}
Provides:       tex(unikaibe.tfm) = %{tl_version}, tex(unikaibf.tfm) = %{tl_version}
Provides:       tex(unikaic0.tfm) = %{tl_version}, tex(unikaic1.tfm) = %{tl_version}
Provides:       tex(unikaic2.tfm) = %{tl_version}, tex(unikaic3.tfm) = %{tl_version}
Provides:       tex(unikaic4.tfm) = %{tl_version}, tex(unikaic5.tfm) = %{tl_version}
Provides:       tex(unikaic6.tfm) = %{tl_version}, tex(unikaic7.tfm) = %{tl_version}
Provides:       tex(unikaic8.tfm) = %{tl_version}, tex(unikaic9.tfm) = %{tl_version}
Provides:       tex(unikaica.tfm) = %{tl_version}, tex(unikaicb.tfm) = %{tl_version}
Provides:       tex(unikaicc.tfm) = %{tl_version}, tex(unikaicd.tfm) = %{tl_version}
Provides:       tex(unikaice.tfm) = %{tl_version}, tex(unikaicf.tfm) = %{tl_version}
Provides:       tex(unikaid0.tfm) = %{tl_version}, tex(unikaid1.tfm) = %{tl_version}
Provides:       tex(unikaid2.tfm) = %{tl_version}, tex(unikaid3.tfm) = %{tl_version}
Provides:       tex(unikaid4.tfm) = %{tl_version}, tex(unikaid5.tfm) = %{tl_version}
Provides:       tex(unikaid6.tfm) = %{tl_version}, tex(unikaid7.tfm) = %{tl_version}
Provides:       tex(unikaid8.tfm) = %{tl_version}, tex(unikaid9.tfm) = %{tl_version}
Provides:       tex(unikaida.tfm) = %{tl_version}, tex(unikaidb.tfm) = %{tl_version}
Provides:       tex(unikaidc.tfm) = %{tl_version}, tex(unikaidd.tfm) = %{tl_version}
Provides:       tex(unikaide.tfm) = %{tl_version}, tex(unikaidf.tfm) = %{tl_version}
Provides:       tex(unikaie0.tfm) = %{tl_version}, tex(unikaie1.tfm) = %{tl_version}
Provides:       tex(unikaie2.tfm) = %{tl_version}, tex(unikaie3.tfm) = %{tl_version}
Provides:       tex(unikaie4.tfm) = %{tl_version}, tex(unikaie5.tfm) = %{tl_version}
Provides:       tex(unikaie6.tfm) = %{tl_version}, tex(unikaie7.tfm) = %{tl_version}
Provides:       tex(unikaie8.tfm) = %{tl_version}, tex(unikaie9.tfm) = %{tl_version}
Provides:       tex(unikaiea.tfm) = %{tl_version}, tex(unikaieb.tfm) = %{tl_version}
Provides:       tex(unikaiec.tfm) = %{tl_version}, tex(unikaied.tfm) = %{tl_version}
Provides:       tex(unikaiee.tfm) = %{tl_version}, tex(unikaief.tfm) = %{tl_version}
Provides:       tex(unikaif0.tfm) = %{tl_version}, tex(unikaif1.tfm) = %{tl_version}
Provides:       tex(unikaif2.tfm) = %{tl_version}, tex(unikaif3.tfm) = %{tl_version}
Provides:       tex(unikaif4.tfm) = %{tl_version}, tex(unikaif5.tfm) = %{tl_version}
Provides:       tex(unikaif6.tfm) = %{tl_version}, tex(unikaif7.tfm) = %{tl_version}
Provides:       tex(unikaif8.tfm) = %{tl_version}, tex(unikaif9.tfm) = %{tl_version}
Provides:       tex(unikaifa.tfm) = %{tl_version}, tex(unikaifb.tfm) = %{tl_version}
Provides:       tex(unikaifc.tfm) = %{tl_version}, tex(unikaifd.tfm) = %{tl_version}
Provides:       tex(unikaife.tfm) = %{tl_version}, tex(unikaiff.tfm) = %{tl_version}
Provides:       tex(unikaisl00.tfm) = %{tl_version}, tex(unikaisl01.tfm) = %{tl_version}
Provides:       tex(unikaisl02.tfm) = %{tl_version}, tex(unikaisl03.tfm) = %{tl_version}
Provides:       tex(unikaisl04.tfm) = %{tl_version}, tex(unikaisl05.tfm) = %{tl_version}
Provides:       tex(unikaisl06.tfm) = %{tl_version}, tex(unikaisl07.tfm) = %{tl_version}
Provides:       tex(unikaisl08.tfm) = %{tl_version}, tex(unikaisl09.tfm) = %{tl_version}
Provides:       tex(unikaisl0a.tfm) = %{tl_version}, tex(unikaisl0b.tfm) = %{tl_version}
Provides:       tex(unikaisl0c.tfm) = %{tl_version}, tex(unikaisl0d.tfm) = %{tl_version}
Provides:       tex(unikaisl0e.tfm) = %{tl_version}, tex(unikaisl0f.tfm) = %{tl_version}
Provides:       tex(unikaisl10.tfm) = %{tl_version}, tex(unikaisl11.tfm) = %{tl_version}
Provides:       tex(unikaisl12.tfm) = %{tl_version}, tex(unikaisl13.tfm) = %{tl_version}
Provides:       tex(unikaisl14.tfm) = %{tl_version}, tex(unikaisl15.tfm) = %{tl_version}
Provides:       tex(unikaisl16.tfm) = %{tl_version}, tex(unikaisl17.tfm) = %{tl_version}
Provides:       tex(unikaisl18.tfm) = %{tl_version}, tex(unikaisl19.tfm) = %{tl_version}
Provides:       tex(unikaisl1a.tfm) = %{tl_version}, tex(unikaisl1b.tfm) = %{tl_version}
Provides:       tex(unikaisl1c.tfm) = %{tl_version}, tex(unikaisl1d.tfm) = %{tl_version}
Provides:       tex(unikaisl1e.tfm) = %{tl_version}, tex(unikaisl1f.tfm) = %{tl_version}
Provides:       tex(unikaisl20.tfm) = %{tl_version}, tex(unikaisl21.tfm) = %{tl_version}
Provides:       tex(unikaisl22.tfm) = %{tl_version}, tex(unikaisl23.tfm) = %{tl_version}
Provides:       tex(unikaisl24.tfm) = %{tl_version}, tex(unikaisl25.tfm) = %{tl_version}
Provides:       tex(unikaisl26.tfm) = %{tl_version}, tex(unikaisl27.tfm) = %{tl_version}
Provides:       tex(unikaisl28.tfm) = %{tl_version}, tex(unikaisl29.tfm) = %{tl_version}
Provides:       tex(unikaisl2a.tfm) = %{tl_version}, tex(unikaisl2b.tfm) = %{tl_version}
Provides:       tex(unikaisl2c.tfm) = %{tl_version}, tex(unikaisl2d.tfm) = %{tl_version}
Provides:       tex(unikaisl2e.tfm) = %{tl_version}, tex(unikaisl2f.tfm) = %{tl_version}
Provides:       tex(unikaisl30.tfm) = %{tl_version}, tex(unikaisl31.tfm) = %{tl_version}
Provides:       tex(unikaisl32.tfm) = %{tl_version}, tex(unikaisl33.tfm) = %{tl_version}
Provides:       tex(unikaisl34.tfm) = %{tl_version}, tex(unikaisl35.tfm) = %{tl_version}
Provides:       tex(unikaisl36.tfm) = %{tl_version}, tex(unikaisl37.tfm) = %{tl_version}
Provides:       tex(unikaisl38.tfm) = %{tl_version}, tex(unikaisl39.tfm) = %{tl_version}
Provides:       tex(unikaisl3a.tfm) = %{tl_version}, tex(unikaisl3b.tfm) = %{tl_version}
Provides:       tex(unikaisl3c.tfm) = %{tl_version}, tex(unikaisl3d.tfm) = %{tl_version}
Provides:       tex(unikaisl3e.tfm) = %{tl_version}, tex(unikaisl3f.tfm) = %{tl_version}
Provides:       tex(unikaisl40.tfm) = %{tl_version}, tex(unikaisl41.tfm) = %{tl_version}
Provides:       tex(unikaisl42.tfm) = %{tl_version}, tex(unikaisl43.tfm) = %{tl_version}
Provides:       tex(unikaisl44.tfm) = %{tl_version}, tex(unikaisl45.tfm) = %{tl_version}
Provides:       tex(unikaisl46.tfm) = %{tl_version}, tex(unikaisl47.tfm) = %{tl_version}
Provides:       tex(unikaisl48.tfm) = %{tl_version}, tex(unikaisl49.tfm) = %{tl_version}
Provides:       tex(unikaisl4a.tfm) = %{tl_version}, tex(unikaisl4b.tfm) = %{tl_version}
Provides:       tex(unikaisl4c.tfm) = %{tl_version}, tex(unikaisl4d.tfm) = %{tl_version}
Provides:       tex(unikaisl4e.tfm) = %{tl_version}, tex(unikaisl4f.tfm) = %{tl_version}
Provides:       tex(unikaisl50.tfm) = %{tl_version}, tex(unikaisl51.tfm) = %{tl_version}
Provides:       tex(unikaisl52.tfm) = %{tl_version}, tex(unikaisl53.tfm) = %{tl_version}
Provides:       tex(unikaisl54.tfm) = %{tl_version}, tex(unikaisl55.tfm) = %{tl_version}
Provides:       tex(unikaisl56.tfm) = %{tl_version}, tex(unikaisl57.tfm) = %{tl_version}
Provides:       tex(unikaisl58.tfm) = %{tl_version}, tex(unikaisl59.tfm) = %{tl_version}
Provides:       tex(unikaisl5a.tfm) = %{tl_version}, tex(unikaisl5b.tfm) = %{tl_version}
Provides:       tex(unikaisl5c.tfm) = %{tl_version}, tex(unikaisl5d.tfm) = %{tl_version}
Provides:       tex(unikaisl5e.tfm) = %{tl_version}, tex(unikaisl5f.tfm) = %{tl_version}
Provides:       tex(unikaisl60.tfm) = %{tl_version}, tex(unikaisl61.tfm) = %{tl_version}
Provides:       tex(unikaisl62.tfm) = %{tl_version}, tex(unikaisl63.tfm) = %{tl_version}
Provides:       tex(unikaisl64.tfm) = %{tl_version}, tex(unikaisl65.tfm) = %{tl_version}
Provides:       tex(unikaisl66.tfm) = %{tl_version}, tex(unikaisl67.tfm) = %{tl_version}
Provides:       tex(unikaisl68.tfm) = %{tl_version}, tex(unikaisl69.tfm) = %{tl_version}
Provides:       tex(unikaisl6a.tfm) = %{tl_version}, tex(unikaisl6b.tfm) = %{tl_version}
Provides:       tex(unikaisl6c.tfm) = %{tl_version}, tex(unikaisl6d.tfm) = %{tl_version}
Provides:       tex(unikaisl6e.tfm) = %{tl_version}, tex(unikaisl6f.tfm) = %{tl_version}
Provides:       tex(unikaisl70.tfm) = %{tl_version}, tex(unikaisl71.tfm) = %{tl_version}
Provides:       tex(unikaisl72.tfm) = %{tl_version}, tex(unikaisl73.tfm) = %{tl_version}
Provides:       tex(unikaisl74.tfm) = %{tl_version}, tex(unikaisl75.tfm) = %{tl_version}
Provides:       tex(unikaisl76.tfm) = %{tl_version}, tex(unikaisl77.tfm) = %{tl_version}
Provides:       tex(unikaisl78.tfm) = %{tl_version}, tex(unikaisl79.tfm) = %{tl_version}
Provides:       tex(unikaisl7a.tfm) = %{tl_version}, tex(unikaisl7b.tfm) = %{tl_version}
Provides:       tex(unikaisl7c.tfm) = %{tl_version}, tex(unikaisl7d.tfm) = %{tl_version}
Provides:       tex(unikaisl7e.tfm) = %{tl_version}, tex(unikaisl7f.tfm) = %{tl_version}
Provides:       tex(unikaisl80.tfm) = %{tl_version}, tex(unikaisl81.tfm) = %{tl_version}
Provides:       tex(unikaisl82.tfm) = %{tl_version}, tex(unikaisl83.tfm) = %{tl_version}
Provides:       tex(unikaisl84.tfm) = %{tl_version}, tex(unikaisl85.tfm) = %{tl_version}
Provides:       tex(unikaisl86.tfm) = %{tl_version}, tex(unikaisl87.tfm) = %{tl_version}
Provides:       tex(unikaisl88.tfm) = %{tl_version}, tex(unikaisl89.tfm) = %{tl_version}
Provides:       tex(unikaisl8a.tfm) = %{tl_version}, tex(unikaisl8b.tfm) = %{tl_version}
Provides:       tex(unikaisl8c.tfm) = %{tl_version}, tex(unikaisl8d.tfm) = %{tl_version}
Provides:       tex(unikaisl8e.tfm) = %{tl_version}, tex(unikaisl8f.tfm) = %{tl_version}
Provides:       tex(unikaisl90.tfm) = %{tl_version}, tex(unikaisl91.tfm) = %{tl_version}
Provides:       tex(unikaisl92.tfm) = %{tl_version}, tex(unikaisl93.tfm) = %{tl_version}
Provides:       tex(unikaisl94.tfm) = %{tl_version}, tex(unikaisl95.tfm) = %{tl_version}
Provides:       tex(unikaisl96.tfm) = %{tl_version}, tex(unikaisl97.tfm) = %{tl_version}
Provides:       tex(unikaisl98.tfm) = %{tl_version}, tex(unikaisl99.tfm) = %{tl_version}
Provides:       tex(unikaisl9a.tfm) = %{tl_version}, tex(unikaisl9b.tfm) = %{tl_version}
Provides:       tex(unikaisl9c.tfm) = %{tl_version}, tex(unikaisl9d.tfm) = %{tl_version}
Provides:       tex(unikaisl9e.tfm) = %{tl_version}, tex(unikaisl9f.tfm) = %{tl_version}
Provides:       tex(unikaisla0.tfm) = %{tl_version}, tex(unikaisla1.tfm) = %{tl_version}
Provides:       tex(unikaisla2.tfm) = %{tl_version}, tex(unikaisla3.tfm) = %{tl_version}
Provides:       tex(unikaisla4.tfm) = %{tl_version}, tex(unikaisla5.tfm) = %{tl_version}
Provides:       tex(unikaisla6.tfm) = %{tl_version}, tex(unikaisla7.tfm) = %{tl_version}
Provides:       tex(unikaisla8.tfm) = %{tl_version}, tex(unikaisla9.tfm) = %{tl_version}
Provides:       tex(unikaislaa.tfm) = %{tl_version}, tex(unikaislab.tfm) = %{tl_version}
Provides:       tex(unikaislac.tfm) = %{tl_version}, tex(unikaislad.tfm) = %{tl_version}
Provides:       tex(unikaislae.tfm) = %{tl_version}, tex(unikaislaf.tfm) = %{tl_version}
Provides:       tex(unikaislb0.tfm) = %{tl_version}, tex(unikaislb1.tfm) = %{tl_version}
Provides:       tex(unikaislb2.tfm) = %{tl_version}, tex(unikaislb3.tfm) = %{tl_version}
Provides:       tex(unikaislb4.tfm) = %{tl_version}, tex(unikaislb5.tfm) = %{tl_version}
Provides:       tex(unikaislb6.tfm) = %{tl_version}, tex(unikaislb7.tfm) = %{tl_version}
Provides:       tex(unikaislb8.tfm) = %{tl_version}, tex(unikaislb9.tfm) = %{tl_version}
Provides:       tex(unikaislba.tfm) = %{tl_version}, tex(unikaislbb.tfm) = %{tl_version}
Provides:       tex(unikaislbc.tfm) = %{tl_version}, tex(unikaislbd.tfm) = %{tl_version}
Provides:       tex(unikaislbe.tfm) = %{tl_version}, tex(unikaislbf.tfm) = %{tl_version}
Provides:       tex(unikaislc0.tfm) = %{tl_version}, tex(unikaislc1.tfm) = %{tl_version}
Provides:       tex(unikaislc2.tfm) = %{tl_version}, tex(unikaislc3.tfm) = %{tl_version}
Provides:       tex(unikaislc4.tfm) = %{tl_version}, tex(unikaislc5.tfm) = %{tl_version}
Provides:       tex(unikaislc6.tfm) = %{tl_version}, tex(unikaislc7.tfm) = %{tl_version}
Provides:       tex(unikaislc8.tfm) = %{tl_version}, tex(unikaislc9.tfm) = %{tl_version}
Provides:       tex(unikaislca.tfm) = %{tl_version}, tex(unikaislcb.tfm) = %{tl_version}
Provides:       tex(unikaislcc.tfm) = %{tl_version}, tex(unikaislcd.tfm) = %{tl_version}
Provides:       tex(unikaislce.tfm) = %{tl_version}, tex(unikaislcf.tfm) = %{tl_version}
Provides:       tex(unikaisld0.tfm) = %{tl_version}, tex(unikaisld1.tfm) = %{tl_version}
Provides:       tex(unikaisld2.tfm) = %{tl_version}, tex(unikaisld3.tfm) = %{tl_version}
Provides:       tex(unikaisld4.tfm) = %{tl_version}, tex(unikaisld5.tfm) = %{tl_version}
Provides:       tex(unikaisld6.tfm) = %{tl_version}, tex(unikaisld7.tfm) = %{tl_version}
Provides:       tex(unikaisld8.tfm) = %{tl_version}, tex(unikaisld9.tfm) = %{tl_version}
Provides:       tex(unikaislda.tfm) = %{tl_version}, tex(unikaisldb.tfm) = %{tl_version}
Provides:       tex(unikaisldc.tfm) = %{tl_version}, tex(unikaisldd.tfm) = %{tl_version}
Provides:       tex(unikaislde.tfm) = %{tl_version}, tex(unikaisldf.tfm) = %{tl_version}
Provides:       tex(unikaisle0.tfm) = %{tl_version}, tex(unikaisle1.tfm) = %{tl_version}
Provides:       tex(unikaisle2.tfm) = %{tl_version}, tex(unikaisle3.tfm) = %{tl_version}
Provides:       tex(unikaisle4.tfm) = %{tl_version}, tex(unikaisle5.tfm) = %{tl_version}
Provides:       tex(unikaisle6.tfm) = %{tl_version}, tex(unikaisle7.tfm) = %{tl_version}
Provides:       tex(unikaisle8.tfm) = %{tl_version}, tex(unikaisle9.tfm) = %{tl_version}
Provides:       tex(unikaislea.tfm) = %{tl_version}, tex(unikaisleb.tfm) = %{tl_version}
Provides:       tex(unikaislec.tfm) = %{tl_version}, tex(unikaisled.tfm) = %{tl_version}
Provides:       tex(unikaislee.tfm) = %{tl_version}, tex(unikaislef.tfm) = %{tl_version}
Provides:       tex(unikaislf0.tfm) = %{tl_version}, tex(unikaislf1.tfm) = %{tl_version}
Provides:       tex(unikaislf2.tfm) = %{tl_version}, tex(unikaislf3.tfm) = %{tl_version}
Provides:       tex(unikaislf4.tfm) = %{tl_version}, tex(unikaislf5.tfm) = %{tl_version}
Provides:       tex(unikaislf6.tfm) = %{tl_version}, tex(unikaislf7.tfm) = %{tl_version}
Provides:       tex(unikaislf8.tfm) = %{tl_version}, tex(unikaislf9.tfm) = %{tl_version}
Provides:       tex(unikaislfa.tfm) = %{tl_version}, tex(unikaislfb.tfm) = %{tl_version}
Provides:       tex(unikaislfc.tfm) = %{tl_version}, tex(unikaislfd.tfm) = %{tl_version}
Provides:       tex(unikaislfe.tfm) = %{tl_version}, tex(unikaislff.tfm) = %{tl_version}
Provides:       tex(unili00.tfm) = %{tl_version}, tex(unili01.tfm) = %{tl_version}
Provides:       tex(unili02.tfm) = %{tl_version}, tex(unili03.tfm) = %{tl_version}
Provides:       tex(unili04.tfm) = %{tl_version}, tex(unili05.tfm) = %{tl_version}
Provides:       tex(unili06.tfm) = %{tl_version}, tex(unili07.tfm) = %{tl_version}
Provides:       tex(unili08.tfm) = %{tl_version}, tex(unili09.tfm) = %{tl_version}
Provides:       tex(unili0a.tfm) = %{tl_version}, tex(unili0b.tfm) = %{tl_version}
Provides:       tex(unili0c.tfm) = %{tl_version}, tex(unili0d.tfm) = %{tl_version}
Provides:       tex(unili0e.tfm) = %{tl_version}, tex(unili0f.tfm) = %{tl_version}
Provides:       tex(unili10.tfm) = %{tl_version}, tex(unili11.tfm) = %{tl_version}
Provides:       tex(unili12.tfm) = %{tl_version}, tex(unili13.tfm) = %{tl_version}
Provides:       tex(unili14.tfm) = %{tl_version}, tex(unili15.tfm) = %{tl_version}
Provides:       tex(unili16.tfm) = %{tl_version}, tex(unili17.tfm) = %{tl_version}
Provides:       tex(unili18.tfm) = %{tl_version}, tex(unili19.tfm) = %{tl_version}
Provides:       tex(unili1a.tfm) = %{tl_version}, tex(unili1b.tfm) = %{tl_version}
Provides:       tex(unili1c.tfm) = %{tl_version}, tex(unili1d.tfm) = %{tl_version}
Provides:       tex(unili1e.tfm) = %{tl_version}, tex(unili1f.tfm) = %{tl_version}
Provides:       tex(unili20.tfm) = %{tl_version}, tex(unili21.tfm) = %{tl_version}
Provides:       tex(unili22.tfm) = %{tl_version}, tex(unili23.tfm) = %{tl_version}
Provides:       tex(unili24.tfm) = %{tl_version}, tex(unili25.tfm) = %{tl_version}
Provides:       tex(unili26.tfm) = %{tl_version}, tex(unili27.tfm) = %{tl_version}
Provides:       tex(unili28.tfm) = %{tl_version}, tex(unili29.tfm) = %{tl_version}
Provides:       tex(unili2a.tfm) = %{tl_version}, tex(unili2b.tfm) = %{tl_version}
Provides:       tex(unili2c.tfm) = %{tl_version}, tex(unili2d.tfm) = %{tl_version}
Provides:       tex(unili2e.tfm) = %{tl_version}, tex(unili2f.tfm) = %{tl_version}
Provides:       tex(unili30.tfm) = %{tl_version}, tex(unili31.tfm) = %{tl_version}
Provides:       tex(unili32.tfm) = %{tl_version}, tex(unili33.tfm) = %{tl_version}
Provides:       tex(unili34.tfm) = %{tl_version}, tex(unili35.tfm) = %{tl_version}
Provides:       tex(unili36.tfm) = %{tl_version}, tex(unili37.tfm) = %{tl_version}
Provides:       tex(unili38.tfm) = %{tl_version}, tex(unili39.tfm) = %{tl_version}
Provides:       tex(unili3a.tfm) = %{tl_version}, tex(unili3b.tfm) = %{tl_version}
Provides:       tex(unili3c.tfm) = %{tl_version}, tex(unili3d.tfm) = %{tl_version}
Provides:       tex(unili3e.tfm) = %{tl_version}, tex(unili3f.tfm) = %{tl_version}
Provides:       tex(unili40.tfm) = %{tl_version}, tex(unili41.tfm) = %{tl_version}
Provides:       tex(unili42.tfm) = %{tl_version}, tex(unili43.tfm) = %{tl_version}
Provides:       tex(unili44.tfm) = %{tl_version}, tex(unili45.tfm) = %{tl_version}
Provides:       tex(unili46.tfm) = %{tl_version}, tex(unili47.tfm) = %{tl_version}
Provides:       tex(unili48.tfm) = %{tl_version}, tex(unili49.tfm) = %{tl_version}
Provides:       tex(unili4a.tfm) = %{tl_version}, tex(unili4b.tfm) = %{tl_version}
Provides:       tex(unili4c.tfm) = %{tl_version}, tex(unili4d.tfm) = %{tl_version}
Provides:       tex(unili4e.tfm) = %{tl_version}, tex(unili4f.tfm) = %{tl_version}
Provides:       tex(unili50.tfm) = %{tl_version}, tex(unili51.tfm) = %{tl_version}
Provides:       tex(unili52.tfm) = %{tl_version}, tex(unili53.tfm) = %{tl_version}
Provides:       tex(unili54.tfm) = %{tl_version}, tex(unili55.tfm) = %{tl_version}
Provides:       tex(unili56.tfm) = %{tl_version}, tex(unili57.tfm) = %{tl_version}
Provides:       tex(unili58.tfm) = %{tl_version}, tex(unili59.tfm) = %{tl_version}
Provides:       tex(unili5a.tfm) = %{tl_version}, tex(unili5b.tfm) = %{tl_version}
Provides:       tex(unili5c.tfm) = %{tl_version}, tex(unili5d.tfm) = %{tl_version}
Provides:       tex(unili5e.tfm) = %{tl_version}, tex(unili5f.tfm) = %{tl_version}
Provides:       tex(unili60.tfm) = %{tl_version}, tex(unili61.tfm) = %{tl_version}
Provides:       tex(unili62.tfm) = %{tl_version}, tex(unili63.tfm) = %{tl_version}
Provides:       tex(unili64.tfm) = %{tl_version}, tex(unili65.tfm) = %{tl_version}
Provides:       tex(unili66.tfm) = %{tl_version}, tex(unili67.tfm) = %{tl_version}
Provides:       tex(unili68.tfm) = %{tl_version}, tex(unili69.tfm) = %{tl_version}
Provides:       tex(unili6a.tfm) = %{tl_version}, tex(unili6b.tfm) = %{tl_version}
Provides:       tex(unili6c.tfm) = %{tl_version}, tex(unili6d.tfm) = %{tl_version}
Provides:       tex(unili6e.tfm) = %{tl_version}, tex(unili6f.tfm) = %{tl_version}
Provides:       tex(unili70.tfm) = %{tl_version}, tex(unili71.tfm) = %{tl_version}
Provides:       tex(unili72.tfm) = %{tl_version}, tex(unili73.tfm) = %{tl_version}
Provides:       tex(unili74.tfm) = %{tl_version}, tex(unili75.tfm) = %{tl_version}
Provides:       tex(unili76.tfm) = %{tl_version}, tex(unili77.tfm) = %{tl_version}
Provides:       tex(unili78.tfm) = %{tl_version}, tex(unili79.tfm) = %{tl_version}
Provides:       tex(unili7a.tfm) = %{tl_version}, tex(unili7b.tfm) = %{tl_version}
Provides:       tex(unili7c.tfm) = %{tl_version}, tex(unili7d.tfm) = %{tl_version}
Provides:       tex(unili7e.tfm) = %{tl_version}, tex(unili7f.tfm) = %{tl_version}
Provides:       tex(unili80.tfm) = %{tl_version}, tex(unili81.tfm) = %{tl_version}
Provides:       tex(unili82.tfm) = %{tl_version}, tex(unili83.tfm) = %{tl_version}
Provides:       tex(unili84.tfm) = %{tl_version}, tex(unili85.tfm) = %{tl_version}
Provides:       tex(unili86.tfm) = %{tl_version}, tex(unili87.tfm) = %{tl_version}
Provides:       tex(unili88.tfm) = %{tl_version}, tex(unili89.tfm) = %{tl_version}
Provides:       tex(unili8a.tfm) = %{tl_version}, tex(unili8b.tfm) = %{tl_version}
Provides:       tex(unili8c.tfm) = %{tl_version}, tex(unili8d.tfm) = %{tl_version}
Provides:       tex(unili8e.tfm) = %{tl_version}, tex(unili8f.tfm) = %{tl_version}
Provides:       tex(unili90.tfm) = %{tl_version}, tex(unili91.tfm) = %{tl_version}
Provides:       tex(unili92.tfm) = %{tl_version}, tex(unili93.tfm) = %{tl_version}
Provides:       tex(unili94.tfm) = %{tl_version}, tex(unili95.tfm) = %{tl_version}
Provides:       tex(unili96.tfm) = %{tl_version}, tex(unili97.tfm) = %{tl_version}
Provides:       tex(unili98.tfm) = %{tl_version}, tex(unili99.tfm) = %{tl_version}
Provides:       tex(unili9a.tfm) = %{tl_version}, tex(unili9b.tfm) = %{tl_version}
Provides:       tex(unili9c.tfm) = %{tl_version}, tex(unili9d.tfm) = %{tl_version}
Provides:       tex(unili9e.tfm) = %{tl_version}, tex(unili9f.tfm) = %{tl_version}
Provides:       tex(unilia0.tfm) = %{tl_version}, tex(unilia1.tfm) = %{tl_version}
Provides:       tex(unilia2.tfm) = %{tl_version}, tex(unilia3.tfm) = %{tl_version}
Provides:       tex(unilia4.tfm) = %{tl_version}, tex(unilia5.tfm) = %{tl_version}
Provides:       tex(unilia6.tfm) = %{tl_version}, tex(unilia7.tfm) = %{tl_version}
Provides:       tex(unilia8.tfm) = %{tl_version}, tex(unilia9.tfm) = %{tl_version}
Provides:       tex(uniliaa.tfm) = %{tl_version}, tex(uniliab.tfm) = %{tl_version}
Provides:       tex(uniliac.tfm) = %{tl_version}, tex(uniliad.tfm) = %{tl_version}
Provides:       tex(uniliae.tfm) = %{tl_version}, tex(uniliaf.tfm) = %{tl_version}
Provides:       tex(unilib0.tfm) = %{tl_version}, tex(unilib1.tfm) = %{tl_version}
Provides:       tex(unilib2.tfm) = %{tl_version}, tex(unilib3.tfm) = %{tl_version}
Provides:       tex(unilib4.tfm) = %{tl_version}, tex(unilib5.tfm) = %{tl_version}
Provides:       tex(unilib6.tfm) = %{tl_version}, tex(unilib7.tfm) = %{tl_version}
Provides:       tex(unilib8.tfm) = %{tl_version}, tex(unilib9.tfm) = %{tl_version}
Provides:       tex(uniliba.tfm) = %{tl_version}, tex(unilibb.tfm) = %{tl_version}
Provides:       tex(unilibc.tfm) = %{tl_version}, tex(unilibd.tfm) = %{tl_version}
Provides:       tex(unilibe.tfm) = %{tl_version}, tex(unilibf.tfm) = %{tl_version}
Provides:       tex(unilic0.tfm) = %{tl_version}, tex(unilic1.tfm) = %{tl_version}
Provides:       tex(unilic2.tfm) = %{tl_version}, tex(unilic3.tfm) = %{tl_version}
Provides:       tex(unilic4.tfm) = %{tl_version}, tex(unilic5.tfm) = %{tl_version}
Provides:       tex(unilic6.tfm) = %{tl_version}, tex(unilic7.tfm) = %{tl_version}
Provides:       tex(unilic8.tfm) = %{tl_version}, tex(unilic9.tfm) = %{tl_version}
Provides:       tex(unilica.tfm) = %{tl_version}, tex(unilicb.tfm) = %{tl_version}
Provides:       tex(unilicc.tfm) = %{tl_version}, tex(unilicd.tfm) = %{tl_version}
Provides:       tex(unilice.tfm) = %{tl_version}, tex(unilicf.tfm) = %{tl_version}
Provides:       tex(unilid0.tfm) = %{tl_version}, tex(unilid1.tfm) = %{tl_version}
Provides:       tex(unilid2.tfm) = %{tl_version}, tex(unilid3.tfm) = %{tl_version}
Provides:       tex(unilid4.tfm) = %{tl_version}, tex(unilid5.tfm) = %{tl_version}
Provides:       tex(unilid6.tfm) = %{tl_version}, tex(unilid7.tfm) = %{tl_version}
Provides:       tex(unilid8.tfm) = %{tl_version}, tex(unilid9.tfm) = %{tl_version}
Provides:       tex(unilida.tfm) = %{tl_version}, tex(unilidb.tfm) = %{tl_version}
Provides:       tex(unilidc.tfm) = %{tl_version}, tex(unilidd.tfm) = %{tl_version}
Provides:       tex(unilide.tfm) = %{tl_version}, tex(unilidf.tfm) = %{tl_version}
Provides:       tex(unilie0.tfm) = %{tl_version}, tex(unilie1.tfm) = %{tl_version}
Provides:       tex(unilie2.tfm) = %{tl_version}, tex(unilie3.tfm) = %{tl_version}
Provides:       tex(unilie4.tfm) = %{tl_version}, tex(unilie5.tfm) = %{tl_version}
Provides:       tex(unilie6.tfm) = %{tl_version}, tex(unilie7.tfm) = %{tl_version}
Provides:       tex(unilie8.tfm) = %{tl_version}, tex(unilie9.tfm) = %{tl_version}
Provides:       tex(uniliea.tfm) = %{tl_version}, tex(unilieb.tfm) = %{tl_version}
Provides:       tex(uniliec.tfm) = %{tl_version}, tex(unilied.tfm) = %{tl_version}
Provides:       tex(uniliee.tfm) = %{tl_version}, tex(unilief.tfm) = %{tl_version}
Provides:       tex(unilif0.tfm) = %{tl_version}, tex(unilif1.tfm) = %{tl_version}
Provides:       tex(unilif2.tfm) = %{tl_version}, tex(unilif3.tfm) = %{tl_version}
Provides:       tex(unilif4.tfm) = %{tl_version}, tex(unilif5.tfm) = %{tl_version}
Provides:       tex(unilif6.tfm) = %{tl_version}, tex(unilif7.tfm) = %{tl_version}
Provides:       tex(unilif8.tfm) = %{tl_version}, tex(unilif9.tfm) = %{tl_version}
Provides:       tex(unilif8.tfm) = %{tl_version}, tex(unilif9.tfm) = %{tl_version}
Provides:       tex(unilifa.tfm) = %{tl_version}, tex(unilifb.tfm) = %{tl_version}
Provides:       tex(unilifc.tfm) = %{tl_version}, tex(unilifd.tfm) = %{tl_version}
Provides:       tex(unilife.tfm) = %{tl_version}, tex(uniliff.tfm) = %{tl_version}
Provides:       tex(unilisl00.tfm) = %{tl_version}, tex(unilisl01.tfm) = %{tl_version}
Provides:       tex(unilisl02.tfm) = %{tl_version}, tex(unilisl03.tfm) = %{tl_version}
Provides:       tex(unilisl04.tfm) = %{tl_version}, tex(unilisl05.tfm) = %{tl_version}
Provides:       tex(unilisl06.tfm) = %{tl_version}, tex(unilisl07.tfm) = %{tl_version}
Provides:       tex(unilisl08.tfm) = %{tl_version}, tex(unilisl09.tfm) = %{tl_version}
Provides:       tex(unilisl0a.tfm) = %{tl_version}, tex(unilisl0b.tfm) = %{tl_version}
Provides:       tex(unilisl0c.tfm) = %{tl_version}, tex(unilisl0d.tfm) = %{tl_version}
Provides:       tex(unilisl0e.tfm) = %{tl_version}, tex(unilisl0f.tfm) = %{tl_version}
Provides:       tex(unilisl10.tfm) = %{tl_version}, tex(unilisl11.tfm) = %{tl_version}
Provides:       tex(unilisl12.tfm) = %{tl_version}, tex(unilisl13.tfm) = %{tl_version}
Provides:       tex(unilisl14.tfm) = %{tl_version}, tex(unilisl15.tfm) = %{tl_version}
Provides:       tex(unilisl16.tfm) = %{tl_version}, tex(unilisl17.tfm) = %{tl_version}
Provides:       tex(unilisl18.tfm) = %{tl_version}, tex(unilisl19.tfm) = %{tl_version}
Provides:       tex(unilisl1a.tfm) = %{tl_version}, tex(unilisl1b.tfm) = %{tl_version}
Provides:       tex(unilisl1c.tfm) = %{tl_version}, tex(unilisl1d.tfm) = %{tl_version}
Provides:       tex(unilisl1e.tfm) = %{tl_version}, tex(unilisl1f.tfm) = %{tl_version}
Provides:       tex(unilisl20.tfm) = %{tl_version}, tex(unilisl21.tfm) = %{tl_version}
Provides:       tex(unilisl22.tfm) = %{tl_version}, tex(unilisl23.tfm) = %{tl_version}
Provides:       tex(unilisl24.tfm) = %{tl_version}, tex(unilisl25.tfm) = %{tl_version}
Provides:       tex(unilisl26.tfm) = %{tl_version}, tex(unilisl27.tfm) = %{tl_version}
Provides:       tex(unilisl28.tfm) = %{tl_version}, tex(unilisl29.tfm) = %{tl_version}
Provides:       tex(unilisl2a.tfm) = %{tl_version}, tex(unilisl2b.tfm) = %{tl_version}
Provides:       tex(unilisl2c.tfm) = %{tl_version}, tex(unilisl2d.tfm) = %{tl_version}
Provides:       tex(unilisl2e.tfm) = %{tl_version}, tex(unilisl2f.tfm) = %{tl_version}
Provides:       tex(unilisl30.tfm) = %{tl_version}, tex(unilisl31.tfm) = %{tl_version}
Provides:       tex(unilisl32.tfm) = %{tl_version}, tex(unilisl33.tfm) = %{tl_version}
Provides:       tex(unilisl34.tfm) = %{tl_version}, tex(unilisl35.tfm) = %{tl_version}
Provides:       tex(unilisl36.tfm) = %{tl_version}, tex(unilisl37.tfm) = %{tl_version}
Provides:       tex(unilisl38.tfm) = %{tl_version}, tex(unilisl39.tfm) = %{tl_version}
Provides:       tex(unilisl3a.tfm) = %{tl_version}, tex(unilisl3b.tfm) = %{tl_version}
Provides:       tex(unilisl3c.tfm) = %{tl_version}, tex(unilisl3d.tfm) = %{tl_version}
Provides:       tex(unilisl3e.tfm) = %{tl_version}, tex(unilisl3f.tfm) = %{tl_version}
Provides:       tex(unilisl40.tfm) = %{tl_version}, tex(unilisl41.tfm) = %{tl_version}
Provides:       tex(unilisl42.tfm) = %{tl_version}, tex(unilisl43.tfm) = %{tl_version}
Provides:       tex(unilisl44.tfm) = %{tl_version}, tex(unilisl45.tfm) = %{tl_version}
Provides:       tex(unilisl46.tfm) = %{tl_version}, tex(unilisl47.tfm) = %{tl_version}
Provides:       tex(unilisl48.tfm) = %{tl_version}, tex(unilisl49.tfm) = %{tl_version}
Provides:       tex(unilisl4a.tfm) = %{tl_version}, tex(unilisl4b.tfm) = %{tl_version}
Provides:       tex(unilisl4c.tfm) = %{tl_version}, tex(unilisl4d.tfm) = %{tl_version}
Provides:       tex(unilisl4e.tfm) = %{tl_version}, tex(unilisl4f.tfm) = %{tl_version}
Provides:       tex(unilisl50.tfm) = %{tl_version}, tex(unilisl51.tfm) = %{tl_version}
Provides:       tex(unilisl52.tfm) = %{tl_version}, tex(unilisl53.tfm) = %{tl_version}
Provides:       tex(unilisl54.tfm) = %{tl_version}, tex(unilisl55.tfm) = %{tl_version}
Provides:       tex(unilisl56.tfm) = %{tl_version}, tex(unilisl57.tfm) = %{tl_version}
Provides:       tex(unilisl58.tfm) = %{tl_version}, tex(unilisl59.tfm) = %{tl_version}
Provides:       tex(unilisl5a.tfm) = %{tl_version}, tex(unilisl5b.tfm) = %{tl_version}
Provides:       tex(unilisl5c.tfm) = %{tl_version}, tex(unilisl5d.tfm) = %{tl_version}
Provides:       tex(unilisl5e.tfm) = %{tl_version}, tex(unilisl5f.tfm) = %{tl_version}
Provides:       tex(unilisl60.tfm) = %{tl_version}, tex(unilisl61.tfm) = %{tl_version}
Provides:       tex(unilisl62.tfm) = %{tl_version}, tex(unilisl63.tfm) = %{tl_version}
Provides:       tex(unilisl64.tfm) = %{tl_version}, tex(unilisl65.tfm) = %{tl_version}
Provides:       tex(unilisl66.tfm) = %{tl_version}, tex(unilisl67.tfm) = %{tl_version}
Provides:       tex(unilisl68.tfm) = %{tl_version}, tex(unilisl69.tfm) = %{tl_version}
Provides:       tex(unilisl6a.tfm) = %{tl_version}, tex(unilisl6b.tfm) = %{tl_version}
Provides:       tex(unilisl6c.tfm) = %{tl_version}, tex(unilisl6d.tfm) = %{tl_version}
Provides:       tex(unilisl6e.tfm) = %{tl_version}, tex(unilisl6f.tfm) = %{tl_version}
Provides:       tex(unilisl70.tfm) = %{tl_version}, tex(unilisl71.tfm) = %{tl_version}
Provides:       tex(unilisl72.tfm) = %{tl_version}, tex(unilisl73.tfm) = %{tl_version}
Provides:       tex(unilisl74.tfm) = %{tl_version}, tex(unilisl75.tfm) = %{tl_version}
Provides:       tex(unilisl76.tfm) = %{tl_version}, tex(unilisl77.tfm) = %{tl_version}
Provides:       tex(unilisl78.tfm) = %{tl_version}, tex(unilisl79.tfm) = %{tl_version}
Provides:       tex(unilisl7a.tfm) = %{tl_version}, tex(unilisl7b.tfm) = %{tl_version}
Provides:       tex(unilisl7c.tfm) = %{tl_version}, tex(unilisl7d.tfm) = %{tl_version}
Provides:       tex(unilisl7e.tfm) = %{tl_version}, tex(unilisl7f.tfm) = %{tl_version}
Provides:       tex(unilisl80.tfm) = %{tl_version}, tex(unilisl81.tfm) = %{tl_version}
Provides:       tex(unilisl82.tfm) = %{tl_version}, tex(unilisl83.tfm) = %{tl_version}
Provides:       tex(unilisl84.tfm) = %{tl_version}, tex(unilisl85.tfm) = %{tl_version}
Provides:       tex(unilisl86.tfm) = %{tl_version}, tex(unilisl87.tfm) = %{tl_version}
Provides:       tex(unilisl88.tfm) = %{tl_version}, tex(unilisl89.tfm) = %{tl_version}
Provides:       tex(unilisl8a.tfm) = %{tl_version}, tex(unilisl8b.tfm) = %{tl_version}
Provides:       tex(unilisl8c.tfm) = %{tl_version}, tex(unilisl8d.tfm) = %{tl_version}
Provides:       tex(unilisl8e.tfm) = %{tl_version}, tex(unilisl8f.tfm) = %{tl_version}
Provides:       tex(unilisl90.tfm) = %{tl_version}, tex(unilisl91.tfm) = %{tl_version}
Provides:       tex(unilisl92.tfm) = %{tl_version}, tex(unilisl93.tfm) = %{tl_version}
Provides:       tex(unilisl94.tfm) = %{tl_version}, tex(unilisl95.tfm) = %{tl_version}
Provides:       tex(unilisl96.tfm) = %{tl_version}, tex(unilisl97.tfm) = %{tl_version}
Provides:       tex(unilisl98.tfm) = %{tl_version}, tex(unilisl99.tfm) = %{tl_version}
Provides:       tex(unilisl9a.tfm) = %{tl_version}, tex(unilisl9b.tfm) = %{tl_version}
Provides:       tex(unilisl9c.tfm) = %{tl_version}, tex(unilisl9d.tfm) = %{tl_version}
Provides:       tex(unilisl9e.tfm) = %{tl_version}, tex(unilisl9f.tfm) = %{tl_version}
Provides:       tex(unilisla0.tfm) = %{tl_version}, tex(unilisla1.tfm) = %{tl_version}
Provides:       tex(unilisla2.tfm) = %{tl_version}, tex(unilisla3.tfm) = %{tl_version}
Provides:       tex(unilisla4.tfm) = %{tl_version}, tex(unilisla5.tfm) = %{tl_version}
Provides:       tex(unilisla6.tfm) = %{tl_version}, tex(unilisla7.tfm) = %{tl_version}
Provides:       tex(unilisla8.tfm) = %{tl_version}, tex(unilisla9.tfm) = %{tl_version}
Provides:       tex(unilislaa.tfm) = %{tl_version}, tex(unilislab.tfm) = %{tl_version}
Provides:       tex(unilislac.tfm) = %{tl_version}, tex(unilislad.tfm) = %{tl_version}
Provides:       tex(unilislae.tfm) = %{tl_version}, tex(unilislaf.tfm) = %{tl_version}
Provides:       tex(unilislb0.tfm) = %{tl_version}, tex(unilislb1.tfm) = %{tl_version}
Provides:       tex(unilislb2.tfm) = %{tl_version}, tex(unilislb3.tfm) = %{tl_version}
Provides:       tex(unilislb4.tfm) = %{tl_version}, tex(unilislb5.tfm) = %{tl_version}
Provides:       tex(unilislb6.tfm) = %{tl_version}, tex(unilislb7.tfm) = %{tl_version}
Provides:       tex(unilislb8.tfm) = %{tl_version}, tex(unilislb9.tfm) = %{tl_version}
Provides:       tex(unilislba.tfm) = %{tl_version}, tex(unilislbb.tfm) = %{tl_version}
Provides:       tex(unilislbc.tfm) = %{tl_version}, tex(unilislbd.tfm) = %{tl_version}
Provides:       tex(unilislbe.tfm) = %{tl_version}, tex(unilislbf.tfm) = %{tl_version}
Provides:       tex(unilislc0.tfm) = %{tl_version}, tex(unilislc1.tfm) = %{tl_version}
Provides:       tex(unilislc2.tfm) = %{tl_version}, tex(unilislc3.tfm) = %{tl_version}
Provides:       tex(unilislc4.tfm) = %{tl_version}, tex(unilislc5.tfm) = %{tl_version}
Provides:       tex(unilislc6.tfm) = %{tl_version}, tex(unilislc7.tfm) = %{tl_version}
Provides:       tex(unilislc8.tfm) = %{tl_version}, tex(unilislc9.tfm) = %{tl_version}
Provides:       tex(unilislca.tfm) = %{tl_version}, tex(unilislcb.tfm) = %{tl_version}
Provides:       tex(unilislcc.tfm) = %{tl_version}, tex(unilislcd.tfm) = %{tl_version}
Provides:       tex(unilislce.tfm) = %{tl_version}, tex(unilislcf.tfm) = %{tl_version}
Provides:       tex(unilisld0.tfm) = %{tl_version}, tex(unilisld1.tfm) = %{tl_version}
Provides:       tex(unilisld2.tfm) = %{tl_version}, tex(unilisld3.tfm) = %{tl_version}
Provides:       tex(unilisld4.tfm) = %{tl_version}, tex(unilisld5.tfm) = %{tl_version}
Provides:       tex(unilisld6.tfm) = %{tl_version}, tex(unilisld7.tfm) = %{tl_version}
Provides:       tex(unilisld8.tfm) = %{tl_version}, tex(unilisld9.tfm) = %{tl_version}
Provides:       tex(unilislda.tfm) = %{tl_version}, tex(unilisldb.tfm) = %{tl_version}
Provides:       tex(unilisldc.tfm) = %{tl_version}, tex(unilisldd.tfm) = %{tl_version}
Provides:       tex(unilislde.tfm) = %{tl_version}, tex(unilisldf.tfm) = %{tl_version}
Provides:       tex(unilisle0.tfm) = %{tl_version}, tex(unilisle1.tfm) = %{tl_version}
Provides:       tex(unilisle2.tfm) = %{tl_version}, tex(unilisle3.tfm) = %{tl_version}
Provides:       tex(unilisle4.tfm) = %{tl_version}, tex(unilisle5.tfm) = %{tl_version}
Provides:       tex(unilisle6.tfm) = %{tl_version}, tex(unilisle7.tfm) = %{tl_version}
Provides:       tex(unilisle8.tfm) = %{tl_version}, tex(unilisle9.tfm) = %{tl_version}
Provides:       tex(unilislea.tfm) = %{tl_version}, tex(unilisleb.tfm) = %{tl_version}
Provides:       tex(unilislec.tfm) = %{tl_version}, tex(unilisled.tfm) = %{tl_version}
Provides:       tex(unilislee.tfm) = %{tl_version}, tex(unilislef.tfm) = %{tl_version}
Provides:       tex(unilislf0.tfm) = %{tl_version}, tex(unilislf1.tfm) = %{tl_version}
Provides:       tex(unilislf2.tfm) = %{tl_version}, tex(unilislf3.tfm) = %{tl_version}
Provides:       tex(unilislf4.tfm) = %{tl_version}, tex(unilislf5.tfm) = %{tl_version}
Provides:       tex(unilislf6.tfm) = %{tl_version}, tex(unilislf7.tfm) = %{tl_version}
Provides:       tex(unilislf8.tfm) = %{tl_version}, tex(unilislf9.tfm) = %{tl_version}
Provides:       tex(unilislfa.tfm) = %{tl_version}, tex(unilislfb.tfm) = %{tl_version}
Provides:       tex(unilislfc.tfm) = %{tl_version}, tex(unilislfd.tfm) = %{tl_version}
Provides:       tex(unilislfe.tfm) = %{tl_version}, tex(unilislff.tfm) = %{tl_version}
Provides:       tex(unisong00.tfm) = %{tl_version}, tex(unisong01.tfm) = %{tl_version}
Provides:       tex(unisong02.tfm) = %{tl_version}, tex(unisong03.tfm) = %{tl_version}
Provides:       tex(unisong04.tfm) = %{tl_version}, tex(unisong05.tfm) = %{tl_version}
Provides:       tex(unisong06.tfm) = %{tl_version}, tex(unisong07.tfm) = %{tl_version}
Provides:       tex(unisong08.tfm) = %{tl_version}, tex(unisong09.tfm) = %{tl_version}
Provides:       tex(unisong0a.tfm) = %{tl_version}, tex(unisong0b.tfm) = %{tl_version}
Provides:       tex(unisong0c.tfm) = %{tl_version}, tex(unisong0d.tfm) = %{tl_version}
Provides:       tex(unisong0e.tfm) = %{tl_version}, tex(unisong0f.tfm) = %{tl_version}
Provides:       tex(unisong10.tfm) = %{tl_version}, tex(unisong11.tfm) = %{tl_version}
Provides:       tex(unisong12.tfm) = %{tl_version}, tex(unisong13.tfm) = %{tl_version}
Provides:       tex(unisong14.tfm) = %{tl_version}, tex(unisong15.tfm) = %{tl_version}
Provides:       tex(unisong16.tfm) = %{tl_version}, tex(unisong17.tfm) = %{tl_version}
Provides:       tex(unisong18.tfm) = %{tl_version}, tex(unisong19.tfm) = %{tl_version}
Provides:       tex(unisong1a.tfm) = %{tl_version}, tex(unisong1b.tfm) = %{tl_version}
Provides:       tex(unisong1c.tfm) = %{tl_version}, tex(unisong1d.tfm) = %{tl_version}
Provides:       tex(unisong1e.tfm) = %{tl_version}, tex(unisong1f.tfm) = %{tl_version}
Provides:       tex(unisong20.tfm) = %{tl_version}, tex(unisong21.tfm) = %{tl_version}
Provides:       tex(unisong22.tfm) = %{tl_version}, tex(unisong23.tfm) = %{tl_version}
Provides:       tex(unisong24.tfm) = %{tl_version}, tex(unisong25.tfm) = %{tl_version}
Provides:       tex(unisong26.tfm) = %{tl_version}, tex(unisong27.tfm) = %{tl_version}
Provides:       tex(unisong28.tfm) = %{tl_version}, tex(unisong29.tfm) = %{tl_version}
Provides:       tex(unisong2a.tfm) = %{tl_version}, tex(unisong2b.tfm) = %{tl_version}
Provides:       tex(unisong2c.tfm) = %{tl_version}, tex(unisong2d.tfm) = %{tl_version}
Provides:       tex(unisong2e.tfm) = %{tl_version}, tex(unisong2f.tfm) = %{tl_version}
Provides:       tex(unisong30.tfm) = %{tl_version}, tex(unisong31.tfm) = %{tl_version}
Provides:       tex(unisong32.tfm) = %{tl_version}, tex(unisong33.tfm) = %{tl_version}
Provides:       tex(unisong34.tfm) = %{tl_version}, tex(unisong35.tfm) = %{tl_version}
Provides:       tex(unisong36.tfm) = %{tl_version}, tex(unisong37.tfm) = %{tl_version}
Provides:       tex(unisong38.tfm) = %{tl_version}, tex(unisong39.tfm) = %{tl_version}
Provides:       tex(unisong3a.tfm) = %{tl_version}, tex(unisong3b.tfm) = %{tl_version}
Provides:       tex(unisong3c.tfm) = %{tl_version}, tex(unisong3d.tfm) = %{tl_version}
Provides:       tex(unisong3e.tfm) = %{tl_version}, tex(unisong3f.tfm) = %{tl_version}
Provides:       tex(unisong40.tfm) = %{tl_version}, tex(unisong41.tfm) = %{tl_version}
Provides:       tex(unisong42.tfm) = %{tl_version}, tex(unisong43.tfm) = %{tl_version}
Provides:       tex(unisong44.tfm) = %{tl_version}, tex(unisong45.tfm) = %{tl_version}
Provides:       tex(unisong46.tfm) = %{tl_version}, tex(unisong47.tfm) = %{tl_version}
Provides:       tex(unisong48.tfm) = %{tl_version}, tex(unisong49.tfm) = %{tl_version}
Provides:       tex(unisong4a.tfm) = %{tl_version}, tex(unisong4b.tfm) = %{tl_version}
Provides:       tex(unisong4c.tfm) = %{tl_version}, tex(unisong4d.tfm) = %{tl_version}
Provides:       tex(unisong4e.tfm) = %{tl_version}, tex(unisong4f.tfm) = %{tl_version}
Provides:       tex(unisong50.tfm) = %{tl_version}, tex(unisong51.tfm) = %{tl_version}
Provides:       tex(unisong52.tfm) = %{tl_version}, tex(unisong53.tfm) = %{tl_version}
Provides:       tex(unisong54.tfm) = %{tl_version}, tex(unisong55.tfm) = %{tl_version}
Provides:       tex(unisong56.tfm) = %{tl_version}, tex(unisong57.tfm) = %{tl_version}
Provides:       tex(unisong58.tfm) = %{tl_version}, tex(unisong59.tfm) = %{tl_version}
Provides:       tex(unisong5a.tfm) = %{tl_version}, tex(unisong5b.tfm) = %{tl_version}
Provides:       tex(unisong5c.tfm) = %{tl_version}, tex(unisong5d.tfm) = %{tl_version}
Provides:       tex(unisong5e.tfm) = %{tl_version}, tex(unisong5f.tfm) = %{tl_version}
Provides:       tex(unisong60.tfm) = %{tl_version}, tex(unisong61.tfm) = %{tl_version}
Provides:       tex(unisong62.tfm) = %{tl_version}, tex(unisong63.tfm) = %{tl_version}
Provides:       tex(unisong64.tfm) = %{tl_version}, tex(unisong65.tfm) = %{tl_version}
Provides:       tex(unisong66.tfm) = %{tl_version}, tex(unisong67.tfm) = %{tl_version}
Provides:       tex(unisong68.tfm) = %{tl_version}, tex(unisong69.tfm) = %{tl_version}
Provides:       tex(unisong6a.tfm) = %{tl_version}, tex(unisong6b.tfm) = %{tl_version}
Provides:       tex(unisong6c.tfm) = %{tl_version}, tex(unisong6d.tfm) = %{tl_version}
Provides:       tex(unisong6e.tfm) = %{tl_version}, tex(unisong6f.tfm) = %{tl_version}
Provides:       tex(unisong70.tfm) = %{tl_version}, tex(unisong71.tfm) = %{tl_version}
Provides:       tex(unisong72.tfm) = %{tl_version}, tex(unisong73.tfm) = %{tl_version}
Provides:       tex(unisong74.tfm) = %{tl_version}, tex(unisong75.tfm) = %{tl_version}
Provides:       tex(unisong76.tfm) = %{tl_version}, tex(unisong77.tfm) = %{tl_version}
Provides:       tex(unisong78.tfm) = %{tl_version}, tex(unisong79.tfm) = %{tl_version}
Provides:       tex(unisong7a.tfm) = %{tl_version}, tex(unisong7b.tfm) = %{tl_version}
Provides:       tex(unisong7c.tfm) = %{tl_version}, tex(unisong7d.tfm) = %{tl_version}
Provides:       tex(unisong7e.tfm) = %{tl_version}, tex(unisong7f.tfm) = %{tl_version}
Provides:       tex(unisong80.tfm) = %{tl_version}, tex(unisong81.tfm) = %{tl_version}
Provides:       tex(unisong82.tfm) = %{tl_version}, tex(unisong83.tfm) = %{tl_version}
Provides:       tex(unisong84.tfm) = %{tl_version}, tex(unisong85.tfm) = %{tl_version}
Provides:       tex(unisong86.tfm) = %{tl_version}, tex(unisong87.tfm) = %{tl_version}
Provides:       tex(unisong88.tfm) = %{tl_version}, tex(unisong89.tfm) = %{tl_version}
Provides:       tex(unisong8a.tfm) = %{tl_version}, tex(unisong8b.tfm) = %{tl_version}
Provides:       tex(unisong8c.tfm) = %{tl_version}, tex(unisong8d.tfm) = %{tl_version}
Provides:       tex(unisong8e.tfm) = %{tl_version}, tex(unisong8f.tfm) = %{tl_version}
Provides:       tex(unisong90.tfm) = %{tl_version}, tex(unisong91.tfm) = %{tl_version}
Provides:       tex(unisong92.tfm) = %{tl_version}, tex(unisong93.tfm) = %{tl_version}
Provides:       tex(unisong94.tfm) = %{tl_version}, tex(unisong95.tfm) = %{tl_version}
Provides:       tex(unisong96.tfm) = %{tl_version}, tex(unisong97.tfm) = %{tl_version}
Provides:       tex(unisong98.tfm) = %{tl_version}, tex(unisong99.tfm) = %{tl_version}
Provides:       tex(unisong9a.tfm) = %{tl_version}, tex(unisong9b.tfm) = %{tl_version}
Provides:       tex(unisong9c.tfm) = %{tl_version}, tex(unisong9d.tfm) = %{tl_version}
Provides:       tex(unisong9e.tfm) = %{tl_version}, tex(unisong9f.tfm) = %{tl_version}
Provides:       tex(unisonga0.tfm) = %{tl_version}, tex(unisonga1.tfm) = %{tl_version}
Provides:       tex(unisonga2.tfm) = %{tl_version}, tex(unisonga3.tfm) = %{tl_version}
Provides:       tex(unisonga4.tfm) = %{tl_version}, tex(unisonga5.tfm) = %{tl_version}
Provides:       tex(unisonga6.tfm) = %{tl_version}, tex(unisonga7.tfm) = %{tl_version}
Provides:       tex(unisonga8.tfm) = %{tl_version}, tex(unisonga9.tfm) = %{tl_version}
Provides:       tex(unisongaa.tfm) = %{tl_version}, tex(unisongab.tfm) = %{tl_version}
Provides:       tex(unisongac.tfm) = %{tl_version}, tex(unisongad.tfm) = %{tl_version}
Provides:       tex(unisongae.tfm) = %{tl_version}, tex(unisongaf.tfm) = %{tl_version}
Provides:       tex(unisongb0.tfm) = %{tl_version}, tex(unisongb1.tfm) = %{tl_version}
Provides:       tex(unisongb2.tfm) = %{tl_version}, tex(unisongb3.tfm) = %{tl_version}
Provides:       tex(unisongb4.tfm) = %{tl_version}, tex(unisongb5.tfm) = %{tl_version}
Provides:       tex(unisongb6.tfm) = %{tl_version}, tex(unisongb7.tfm) = %{tl_version}
Provides:       tex(unisongb8.tfm) = %{tl_version}, tex(unisongb9.tfm) = %{tl_version}
Provides:       tex(unisongba.tfm) = %{tl_version}, tex(unisongbb.tfm) = %{tl_version}
Provides:       tex(unisongbc.tfm) = %{tl_version}, tex(unisongbd.tfm) = %{tl_version}
Provides:       tex(unisongbe.tfm) = %{tl_version}, tex(unisongbf.tfm) = %{tl_version}
Provides:       tex(unisongc0.tfm) = %{tl_version}, tex(unisongc1.tfm) = %{tl_version}
Provides:       tex(unisongc2.tfm) = %{tl_version}, tex(unisongc3.tfm) = %{tl_version}
Provides:       tex(unisongc4.tfm) = %{tl_version}, tex(unisongc5.tfm) = %{tl_version}
Provides:       tex(unisongc6.tfm) = %{tl_version}, tex(unisongc7.tfm) = %{tl_version}
Provides:       tex(unisongc8.tfm) = %{tl_version}, tex(unisongc9.tfm) = %{tl_version}
Provides:       tex(unisongca.tfm) = %{tl_version}, tex(unisongcb.tfm) = %{tl_version}
Provides:       tex(unisongcc.tfm) = %{tl_version}, tex(unisongcd.tfm) = %{tl_version}
Provides:       tex(unisongce.tfm) = %{tl_version}, tex(unisongcf.tfm) = %{tl_version}
Provides:       tex(unisongd0.tfm) = %{tl_version}, tex(unisongd1.tfm) = %{tl_version}
Provides:       tex(unisongd2.tfm) = %{tl_version}, tex(unisongd3.tfm) = %{tl_version}
Provides:       tex(unisongd4.tfm) = %{tl_version}, tex(unisongd5.tfm) = %{tl_version}
Provides:       tex(unisongd6.tfm) = %{tl_version}, tex(unisongd7.tfm) = %{tl_version}
Provides:       tex(unisongd8.tfm) = %{tl_version}, tex(unisongd9.tfm) = %{tl_version}
Provides:       tex(unisongda.tfm) = %{tl_version}, tex(unisongdb.tfm) = %{tl_version}
Provides:       tex(unisongdc.tfm) = %{tl_version}, tex(unisongdd.tfm) = %{tl_version}
Provides:       tex(unisongde.tfm) = %{tl_version}, tex(unisongdf.tfm) = %{tl_version}
Provides:       tex(unisonge0.tfm) = %{tl_version}, tex(unisonge1.tfm) = %{tl_version}
Provides:       tex(unisonge2.tfm) = %{tl_version}, tex(unisonge3.tfm) = %{tl_version}
Provides:       tex(unisonge4.tfm) = %{tl_version}, tex(unisonge5.tfm) = %{tl_version}
Provides:       tex(unisonge6.tfm) = %{tl_version}, tex(unisonge7.tfm) = %{tl_version}
Provides:       tex(unisonge8.tfm) = %{tl_version}, tex(unisonge9.tfm) = %{tl_version}
Provides:       tex(unisongea.tfm) = %{tl_version}, tex(unisongeb.tfm) = %{tl_version}
Provides:       tex(unisongec.tfm) = %{tl_version}, tex(unisonged.tfm) = %{tl_version}
Provides:       tex(unisongee.tfm) = %{tl_version}, tex(unisongef.tfm) = %{tl_version}
Provides:       tex(unisongf0.tfm) = %{tl_version}, tex(unisongf1.tfm) = %{tl_version}
Provides:       tex(unisongf2.tfm) = %{tl_version}, tex(unisongf3.tfm) = %{tl_version}
Provides:       tex(unisongf4.tfm) = %{tl_version}, tex(unisongf5.tfm) = %{tl_version}
Provides:       tex(unisongf6.tfm) = %{tl_version}, tex(unisongf7.tfm) = %{tl_version}
Provides:       tex(unisongf8.tfm) = %{tl_version}, tex(unisongf9.tfm) = %{tl_version}
Provides:       tex(unisongfa.tfm) = %{tl_version}, tex(unisongfb.tfm) = %{tl_version}
Provides:       tex(unisongfc.tfm) = %{tl_version}, tex(unisongfd.tfm) = %{tl_version}
Provides:       tex(unisongfe.tfm) = %{tl_version}, tex(unisongff.tfm) = %{tl_version}
Provides:       tex(unisongsl00.tfm) = %{tl_version}, tex(unisongsl01.tfm) = %{tl_version}
Provides:       tex(unisongsl02.tfm) = %{tl_version}, tex(unisongsl03.tfm) = %{tl_version}
Provides:       tex(unisongsl04.tfm) = %{tl_version}, tex(unisongsl05.tfm) = %{tl_version}
Provides:       tex(unisongsl06.tfm) = %{tl_version}, tex(unisongsl07.tfm) = %{tl_version}
Provides:       tex(unisongsl08.tfm) = %{tl_version}, tex(unisongsl09.tfm) = %{tl_version}
Provides:       tex(unisongsl0a.tfm) = %{tl_version}, tex(unisongsl0b.tfm) = %{tl_version}
Provides:       tex(unisongsl0c.tfm) = %{tl_version}, tex(unisongsl0d.tfm) = %{tl_version}
Provides:       tex(unisongsl0e.tfm) = %{tl_version}, tex(unisongsl0f.tfm) = %{tl_version}
Provides:       tex(unisongsl10.tfm) = %{tl_version}, tex(unisongsl11.tfm) = %{tl_version}
Provides:       tex(unisongsl12.tfm) = %{tl_version}, tex(unisongsl13.tfm) = %{tl_version}
Provides:       tex(unisongsl14.tfm) = %{tl_version}, tex(unisongsl15.tfm) = %{tl_version}
Provides:       tex(unisongsl16.tfm) = %{tl_version}, tex(unisongsl17.tfm) = %{tl_version}
Provides:       tex(unisongsl18.tfm) = %{tl_version}, tex(unisongsl19.tfm) = %{tl_version}
Provides:       tex(unisongsl1a.tfm) = %{tl_version}, tex(unisongsl1b.tfm) = %{tl_version}
Provides:       tex(unisongsl1c.tfm) = %{tl_version}, tex(unisongsl1d.tfm) = %{tl_version}
Provides:       tex(unisongsl1e.tfm) = %{tl_version}, tex(unisongsl1f.tfm) = %{tl_version}
Provides:       tex(unisongsl20.tfm) = %{tl_version}, tex(unisongsl21.tfm) = %{tl_version}
Provides:       tex(unisongsl22.tfm) = %{tl_version}, tex(unisongsl23.tfm) = %{tl_version}
Provides:       tex(unisongsl24.tfm) = %{tl_version}, tex(unisongsl25.tfm) = %{tl_version}
Provides:       tex(unisongsl26.tfm) = %{tl_version}, tex(unisongsl27.tfm) = %{tl_version}
Provides:       tex(unisongsl28.tfm) = %{tl_version}, tex(unisongsl29.tfm) = %{tl_version}
Provides:       tex(unisongsl2a.tfm) = %{tl_version}, tex(unisongsl2b.tfm) = %{tl_version}
Provides:       tex(unisongsl2c.tfm) = %{tl_version}, tex(unisongsl2d.tfm) = %{tl_version}
Provides:       tex(unisongsl2e.tfm) = %{tl_version}, tex(unisongsl2f.tfm) = %{tl_version}
Provides:       tex(unisongsl30.tfm) = %{tl_version}, tex(unisongsl31.tfm) = %{tl_version}
Provides:       tex(unisongsl32.tfm) = %{tl_version}, tex(unisongsl33.tfm) = %{tl_version}
Provides:       tex(unisongsl34.tfm) = %{tl_version}, tex(unisongsl35.tfm) = %{tl_version}
Provides:       tex(unisongsl36.tfm) = %{tl_version}, tex(unisongsl37.tfm) = %{tl_version}
Provides:       tex(unisongsl38.tfm) = %{tl_version}, tex(unisongsl39.tfm) = %{tl_version}
Provides:       tex(unisongsl3a.tfm) = %{tl_version}, tex(unisongsl3b.tfm) = %{tl_version}
Provides:       tex(unisongsl3c.tfm) = %{tl_version}, tex(unisongsl3d.tfm) = %{tl_version}
Provides:       tex(unisongsl3e.tfm) = %{tl_version}, tex(unisongsl3f.tfm) = %{tl_version}
Provides:       tex(unisongsl40.tfm) = %{tl_version}, tex(unisongsl41.tfm) = %{tl_version}
Provides:       tex(unisongsl42.tfm) = %{tl_version}, tex(unisongsl43.tfm) = %{tl_version}
Provides:       tex(unisongsl44.tfm) = %{tl_version}, tex(unisongsl45.tfm) = %{tl_version}
Provides:       tex(unisongsl46.tfm) = %{tl_version}, tex(unisongsl47.tfm) = %{tl_version}
Provides:       tex(unisongsl48.tfm) = %{tl_version}, tex(unisongsl49.tfm) = %{tl_version}
Provides:       tex(unisongsl4a.tfm) = %{tl_version}, tex(unisongsl4b.tfm) = %{tl_version}
Provides:       tex(unisongsl4c.tfm) = %{tl_version}, tex(unisongsl4d.tfm) = %{tl_version}
Provides:       tex(unisongsl4e.tfm) = %{tl_version}, tex(unisongsl4f.tfm) = %{tl_version}
Provides:       tex(unisongsl50.tfm) = %{tl_version}, tex(unisongsl51.tfm) = %{tl_version}
Provides:       tex(unisongsl52.tfm) = %{tl_version}, tex(unisongsl53.tfm) = %{tl_version}
Provides:       tex(unisongsl54.tfm) = %{tl_version}, tex(unisongsl55.tfm) = %{tl_version}
Provides:       tex(unisongsl56.tfm) = %{tl_version}, tex(unisongsl57.tfm) = %{tl_version}
Provides:       tex(unisongsl58.tfm) = %{tl_version}, tex(unisongsl59.tfm) = %{tl_version}
Provides:       tex(unisongsl5a.tfm) = %{tl_version}, tex(unisongsl5b.tfm) = %{tl_version}
Provides:       tex(unisongsl5c.tfm) = %{tl_version}, tex(unisongsl5d.tfm) = %{tl_version}
Provides:       tex(unisongsl5e.tfm) = %{tl_version}, tex(unisongsl5f.tfm) = %{tl_version}
Provides:       tex(unisongsl60.tfm) = %{tl_version}, tex(unisongsl61.tfm) = %{tl_version}
Provides:       tex(unisongsl62.tfm) = %{tl_version}, tex(unisongsl63.tfm) = %{tl_version}
Provides:       tex(unisongsl64.tfm) = %{tl_version}, tex(unisongsl65.tfm) = %{tl_version}
Provides:       tex(unisongsl66.tfm) = %{tl_version}, tex(unisongsl67.tfm) = %{tl_version}
Provides:       tex(unisongsl68.tfm) = %{tl_version}, tex(unisongsl69.tfm) = %{tl_version}
Provides:       tex(unisongsl6a.tfm) = %{tl_version}, tex(unisongsl6b.tfm) = %{tl_version}
Provides:       tex(unisongsl6c.tfm) = %{tl_version}, tex(unisongsl6d.tfm) = %{tl_version}
Provides:       tex(unisongsl6e.tfm) = %{tl_version}, tex(unisongsl6f.tfm) = %{tl_version}
Provides:       tex(unisongsl70.tfm) = %{tl_version}, tex(unisongsl71.tfm) = %{tl_version}
Provides:       tex(unisongsl72.tfm) = %{tl_version}, tex(unisongsl73.tfm) = %{tl_version}
Provides:       tex(unisongsl74.tfm) = %{tl_version}, tex(unisongsl75.tfm) = %{tl_version}
Provides:       tex(unisongsl76.tfm) = %{tl_version}, tex(unisongsl77.tfm) = %{tl_version}
Provides:       tex(unisongsl78.tfm) = %{tl_version}, tex(unisongsl79.tfm) = %{tl_version}
Provides:       tex(unisongsl7a.tfm) = %{tl_version}, tex(unisongsl7b.tfm) = %{tl_version}
Provides:       tex(unisongsl7c.tfm) = %{tl_version}, tex(unisongsl7d.tfm) = %{tl_version}
Provides:       tex(unisongsl7e.tfm) = %{tl_version}, tex(unisongsl7f.tfm) = %{tl_version}
Provides:       tex(unisongsl80.tfm) = %{tl_version}, tex(unisongsl81.tfm) = %{tl_version}
Provides:       tex(unisongsl82.tfm) = %{tl_version}, tex(unisongsl83.tfm) = %{tl_version}
Provides:       tex(unisongsl84.tfm) = %{tl_version}, tex(unisongsl85.tfm) = %{tl_version}
Provides:       tex(unisongsl86.tfm) = %{tl_version}, tex(unisongsl87.tfm) = %{tl_version}
Provides:       tex(unisongsl88.tfm) = %{tl_version}, tex(unisongsl89.tfm) = %{tl_version}
Provides:       tex(unisongsl8a.tfm) = %{tl_version}, tex(unisongsl8b.tfm) = %{tl_version}
Provides:       tex(unisongsl8c.tfm) = %{tl_version}, tex(unisongsl8d.tfm) = %{tl_version}
Provides:       tex(unisongsl8e.tfm) = %{tl_version}, tex(unisongsl8f.tfm) = %{tl_version}
Provides:       tex(unisongsl90.tfm) = %{tl_version}, tex(unisongsl91.tfm) = %{tl_version}
Provides:       tex(unisongsl92.tfm) = %{tl_version}, tex(unisongsl93.tfm) = %{tl_version}
Provides:       tex(unisongsl94.tfm) = %{tl_version}, tex(unisongsl95.tfm) = %{tl_version}
Provides:       tex(unisongsl96.tfm) = %{tl_version}, tex(unisongsl97.tfm) = %{tl_version}
Provides:       tex(unisongsl98.tfm) = %{tl_version}, tex(unisongsl99.tfm) = %{tl_version}
Provides:       tex(unisongsl9a.tfm) = %{tl_version}, tex(unisongsl9b.tfm) = %{tl_version}
Provides:       tex(unisongsl9c.tfm) = %{tl_version}, tex(unisongsl9d.tfm) = %{tl_version}
Provides:       tex(unisongsl9e.tfm) = %{tl_version}, tex(unisongsl9f.tfm) = %{tl_version}
Provides:       tex(unisongsla0.tfm) = %{tl_version}, tex(unisongsla1.tfm) = %{tl_version}
Provides:       tex(unisongsla2.tfm) = %{tl_version}, tex(unisongsla3.tfm) = %{tl_version}
Provides:       tex(unisongsla4.tfm) = %{tl_version}, tex(unisongsla5.tfm) = %{tl_version}
Provides:       tex(unisongsla6.tfm) = %{tl_version}, tex(unisongsla7.tfm) = %{tl_version}
Provides:       tex(unisongsla8.tfm) = %{tl_version}, tex(unisongsla9.tfm) = %{tl_version}
Provides:       tex(unisongslaa.tfm) = %{tl_version}, tex(unisongslab.tfm) = %{tl_version}
Provides:       tex(unisongslac.tfm) = %{tl_version}, tex(unisongslad.tfm) = %{tl_version}
Provides:       tex(unisongslae.tfm) = %{tl_version}, tex(unisongslaf.tfm) = %{tl_version}
Provides:       tex(unisongslb0.tfm) = %{tl_version}, tex(unisongslb1.tfm) = %{tl_version}
Provides:       tex(unisongslb2.tfm) = %{tl_version}, tex(unisongslb3.tfm) = %{tl_version}
Provides:       tex(unisongslb4.tfm) = %{tl_version}, tex(unisongslb5.tfm) = %{tl_version}
Provides:       tex(unisongslb6.tfm) = %{tl_version}, tex(unisongslb7.tfm) = %{tl_version}
Provides:       tex(unisongslb8.tfm) = %{tl_version}, tex(unisongslb9.tfm) = %{tl_version}
Provides:       tex(unisongslba.tfm) = %{tl_version}, tex(unisongslbb.tfm) = %{tl_version}
Provides:       tex(unisongslbc.tfm) = %{tl_version}, tex(unisongslbd.tfm) = %{tl_version}
Provides:       tex(unisongslbe.tfm) = %{tl_version}, tex(unisongslbf.tfm) = %{tl_version}
Provides:       tex(unisongslc0.tfm) = %{tl_version}, tex(unisongslc1.tfm) = %{tl_version}
Provides:       tex(unisongslc2.tfm) = %{tl_version}, tex(unisongslc3.tfm) = %{tl_version}
Provides:       tex(unisongslc4.tfm) = %{tl_version}, tex(unisongslc5.tfm) = %{tl_version}
Provides:       tex(unisongslc6.tfm) = %{tl_version}, tex(unisongslc7.tfm) = %{tl_version}
Provides:       tex(unisongslc8.tfm) = %{tl_version}, tex(unisongslc9.tfm) = %{tl_version}
Provides:       tex(unisongslca.tfm) = %{tl_version}, tex(unisongslcb.tfm) = %{tl_version}
Provides:       tex(unisongslcc.tfm) = %{tl_version}, tex(unisongslcd.tfm) = %{tl_version}
Provides:       tex(unisongslce.tfm) = %{tl_version}, tex(unisongslcf.tfm) = %{tl_version}
Provides:       tex(unisongsld0.tfm) = %{tl_version}, tex(unisongsld1.tfm) = %{tl_version}
Provides:       tex(unisongsld2.tfm) = %{tl_version}, tex(unisongsld3.tfm) = %{tl_version}
Provides:       tex(unisongsld4.tfm) = %{tl_version}, tex(unisongsld5.tfm) = %{tl_version}
Provides:       tex(unisongsld6.tfm) = %{tl_version}, tex(unisongsld7.tfm) = %{tl_version}
Provides:       tex(unisongsld8.tfm) = %{tl_version}, tex(unisongsld9.tfm) = %{tl_version}
Provides:       tex(unisongslda.tfm) = %{tl_version}, tex(unisongsldb.tfm) = %{tl_version}
Provides:       tex(unisongsldc.tfm) = %{tl_version}, tex(unisongsldd.tfm) = %{tl_version}
Provides:       tex(unisongslde.tfm) = %{tl_version}, tex(unisongsldf.tfm) = %{tl_version}
Provides:       tex(unisongsle0.tfm) = %{tl_version}, tex(unisongsle1.tfm) = %{tl_version}
Provides:       tex(unisongsle2.tfm) = %{tl_version}, tex(unisongsle3.tfm) = %{tl_version}
Provides:       tex(unisongsle4.tfm) = %{tl_version}, tex(unisongsle5.tfm) = %{tl_version}
Provides:       tex(unisongsle6.tfm) = %{tl_version}, tex(unisongsle7.tfm) = %{tl_version}
Provides:       tex(unisongsle8.tfm) = %{tl_version}, tex(unisongsle9.tfm) = %{tl_version}
Provides:       tex(unisongslea.tfm) = %{tl_version}, tex(unisongsleb.tfm) = %{tl_version}
Provides:       tex(unisongslec.tfm) = %{tl_version}, tex(unisongsled.tfm) = %{tl_version}
Provides:       tex(unisongslee.tfm) = %{tl_version}, tex(unisongslef.tfm) = %{tl_version}
Provides:       tex(unisongslf0.tfm) = %{tl_version}, tex(unisongslf1.tfm) = %{tl_version}
Provides:       tex(unisongslf2.tfm) = %{tl_version}, tex(unisongslf3.tfm) = %{tl_version}
Provides:       tex(unisongslf4.tfm) = %{tl_version}, tex(unisongslf5.tfm) = %{tl_version}
Provides:       tex(unisongslf6.tfm) = %{tl_version}, tex(unisongslf7.tfm) = %{tl_version}
Provides:       tex(unisongslf8.tfm) = %{tl_version}, tex(unisongslf9.tfm) = %{tl_version}
Provides:       tex(unisongslfa.tfm) = %{tl_version}, tex(unisongslfb.tfm) = %{tl_version}
Provides:       tex(unisongslfc.tfm) = %{tl_version}, tex(unisongslfd.tfm) = %{tl_version}
Provides:       tex(unisongslfe.tfm) = %{tl_version}, tex(unisongslff.tfm) = %{tl_version}
Provides:       tex(uniyou00.tfm) = %{tl_version}, tex(uniyou01.tfm) = %{tl_version}
Provides:       tex(uniyou02.tfm) = %{tl_version}, tex(uniyou03.tfm) = %{tl_version}
Provides:       tex(uniyou04.tfm) = %{tl_version}, tex(uniyou05.tfm) = %{tl_version}
Provides:       tex(uniyou06.tfm) = %{tl_version}, tex(uniyou07.tfm) = %{tl_version}
Provides:       tex(uniyou08.tfm) = %{tl_version}, tex(uniyou09.tfm) = %{tl_version}
Provides:       tex(uniyou0a.tfm) = %{tl_version}, tex(uniyou0b.tfm) = %{tl_version}
Provides:       tex(uniyou0c.tfm) = %{tl_version}, tex(uniyou0d.tfm) = %{tl_version}
Provides:       tex(uniyou0e.tfm) = %{tl_version}, tex(uniyou0f.tfm) = %{tl_version}
Provides:       tex(uniyou10.tfm) = %{tl_version}, tex(uniyou11.tfm) = %{tl_version}
Provides:       tex(uniyou12.tfm) = %{tl_version}, tex(uniyou13.tfm) = %{tl_version}
Provides:       tex(uniyou14.tfm) = %{tl_version}, tex(uniyou15.tfm) = %{tl_version}
Provides:       tex(uniyou16.tfm) = %{tl_version}, tex(uniyou17.tfm) = %{tl_version}
Provides:       tex(uniyou18.tfm) = %{tl_version}, tex(uniyou19.tfm) = %{tl_version}
Provides:       tex(uniyou1a.tfm) = %{tl_version}, tex(uniyou1b.tfm) = %{tl_version}
Provides:       tex(uniyou1c.tfm) = %{tl_version}, tex(uniyou1d.tfm) = %{tl_version}
Provides:       tex(uniyou1e.tfm) = %{tl_version}, tex(uniyou1f.tfm) = %{tl_version}
Provides:       tex(uniyou20.tfm) = %{tl_version}, tex(uniyou21.tfm) = %{tl_version}
Provides:       tex(uniyou22.tfm) = %{tl_version}, tex(uniyou23.tfm) = %{tl_version}
Provides:       tex(uniyou24.tfm) = %{tl_version}, tex(uniyou25.tfm) = %{tl_version}
Provides:       tex(uniyou26.tfm) = %{tl_version}, tex(uniyou27.tfm) = %{tl_version}
Provides:       tex(uniyou28.tfm) = %{tl_version}, tex(uniyou29.tfm) = %{tl_version}
Provides:       tex(uniyou2a.tfm) = %{tl_version}, tex(uniyou2b.tfm) = %{tl_version}
Provides:       tex(uniyou2c.tfm) = %{tl_version}, tex(uniyou2d.tfm) = %{tl_version}
Provides:       tex(uniyou2e.tfm) = %{tl_version}, tex(uniyou2f.tfm) = %{tl_version}
Provides:       tex(uniyou30.tfm) = %{tl_version}, tex(uniyou31.tfm) = %{tl_version}
Provides:       tex(uniyou32.tfm) = %{tl_version}, tex(uniyou33.tfm) = %{tl_version}
Provides:       tex(uniyou34.tfm) = %{tl_version}, tex(uniyou35.tfm) = %{tl_version}
Provides:       tex(uniyou36.tfm) = %{tl_version}, tex(uniyou37.tfm) = %{tl_version}
Provides:       tex(uniyou38.tfm) = %{tl_version}, tex(uniyou39.tfm) = %{tl_version}
Provides:       tex(uniyou3a.tfm) = %{tl_version}, tex(uniyou3b.tfm) = %{tl_version}
Provides:       tex(uniyou3c.tfm) = %{tl_version}, tex(uniyou3d.tfm) = %{tl_version}
Provides:       tex(uniyou3e.tfm) = %{tl_version}, tex(uniyou3f.tfm) = %{tl_version}
Provides:       tex(uniyou40.tfm) = %{tl_version}, tex(uniyou41.tfm) = %{tl_version}
Provides:       tex(uniyou42.tfm) = %{tl_version}, tex(uniyou43.tfm) = %{tl_version}
Provides:       tex(uniyou44.tfm) = %{tl_version}, tex(uniyou45.tfm) = %{tl_version}
Provides:       tex(uniyou46.tfm) = %{tl_version}, tex(uniyou47.tfm) = %{tl_version}
Provides:       tex(uniyou48.tfm) = %{tl_version}, tex(uniyou49.tfm) = %{tl_version}
Provides:       tex(uniyou4a.tfm) = %{tl_version}, tex(uniyou4b.tfm) = %{tl_version}
Provides:       tex(uniyou4c.tfm) = %{tl_version}, tex(uniyou4d.tfm) = %{tl_version}
Provides:       tex(uniyou4e.tfm) = %{tl_version}, tex(uniyou4f.tfm) = %{tl_version}
Provides:       tex(uniyou50.tfm) = %{tl_version}, tex(uniyou51.tfm) = %{tl_version}
Provides:       tex(uniyou52.tfm) = %{tl_version}, tex(uniyou53.tfm) = %{tl_version}
Provides:       tex(uniyou54.tfm) = %{tl_version}, tex(uniyou55.tfm) = %{tl_version}
Provides:       tex(uniyou56.tfm) = %{tl_version}, tex(uniyou57.tfm) = %{tl_version}
Provides:       tex(uniyou58.tfm) = %{tl_version}, tex(uniyou59.tfm) = %{tl_version}
Provides:       tex(uniyou5a.tfm) = %{tl_version}, tex(uniyou5b.tfm) = %{tl_version}
Provides:       tex(uniyou5c.tfm) = %{tl_version}, tex(uniyou5d.tfm) = %{tl_version}
Provides:       tex(uniyou5e.tfm) = %{tl_version}, tex(uniyou5f.tfm) = %{tl_version}
Provides:       tex(uniyou60.tfm) = %{tl_version}, tex(uniyou61.tfm) = %{tl_version}
Provides:       tex(uniyou62.tfm) = %{tl_version}, tex(uniyou63.tfm) = %{tl_version}
Provides:       tex(uniyou64.tfm) = %{tl_version}, tex(uniyou65.tfm) = %{tl_version}
Provides:       tex(uniyou66.tfm) = %{tl_version}, tex(uniyou67.tfm) = %{tl_version}
Provides:       tex(uniyou68.tfm) = %{tl_version}, tex(uniyou69.tfm) = %{tl_version}
Provides:       tex(uniyou6a.tfm) = %{tl_version}, tex(uniyou6b.tfm) = %{tl_version}
Provides:       tex(uniyou6c.tfm) = %{tl_version}, tex(uniyou6d.tfm) = %{tl_version}
Provides:       tex(uniyou6e.tfm) = %{tl_version}, tex(uniyou6f.tfm) = %{tl_version}
Provides:       tex(uniyou70.tfm) = %{tl_version}, tex(uniyou71.tfm) = %{tl_version}
Provides:       tex(uniyou72.tfm) = %{tl_version}, tex(uniyou73.tfm) = %{tl_version}
Provides:       tex(uniyou74.tfm) = %{tl_version}, tex(uniyou75.tfm) = %{tl_version}
Provides:       tex(uniyou76.tfm) = %{tl_version}, tex(uniyou77.tfm) = %{tl_version}
Provides:       tex(uniyou78.tfm) = %{tl_version}, tex(uniyou79.tfm) = %{tl_version}
Provides:       tex(uniyou7a.tfm) = %{tl_version}, tex(uniyou7b.tfm) = %{tl_version}
Provides:       tex(uniyou7c.tfm) = %{tl_version}, tex(uniyou7d.tfm) = %{tl_version}
Provides:       tex(uniyou7e.tfm) = %{tl_version}, tex(uniyou7f.tfm) = %{tl_version}
Provides:       tex(uniyou80.tfm) = %{tl_version}, tex(uniyou81.tfm) = %{tl_version}
Provides:       tex(uniyou82.tfm) = %{tl_version}, tex(uniyou83.tfm) = %{tl_version}
Provides:       tex(uniyou84.tfm) = %{tl_version}, tex(uniyou85.tfm) = %{tl_version}
Provides:       tex(uniyou86.tfm) = %{tl_version}, tex(uniyou87.tfm) = %{tl_version}
Provides:       tex(uniyou88.tfm) = %{tl_version}, tex(uniyou89.tfm) = %{tl_version}
Provides:       tex(uniyou8a.tfm) = %{tl_version}, tex(uniyou8b.tfm) = %{tl_version}
Provides:       tex(uniyou8c.tfm) = %{tl_version}, tex(uniyou8d.tfm) = %{tl_version}
Provides:       tex(uniyou8e.tfm) = %{tl_version}, tex(uniyou8f.tfm) = %{tl_version}
Provides:       tex(uniyou90.tfm) = %{tl_version}, tex(uniyou91.tfm) = %{tl_version}
Provides:       tex(uniyou92.tfm) = %{tl_version}, tex(uniyou93.tfm) = %{tl_version}
Provides:       tex(uniyou94.tfm) = %{tl_version}, tex(uniyou95.tfm) = %{tl_version}
Provides:       tex(uniyou96.tfm) = %{tl_version}, tex(uniyou97.tfm) = %{tl_version}
Provides:       tex(uniyou98.tfm) = %{tl_version}, tex(uniyou99.tfm) = %{tl_version}
Provides:       tex(uniyou9a.tfm) = %{tl_version}, tex(uniyou9b.tfm) = %{tl_version}
Provides:       tex(uniyou9c.tfm) = %{tl_version}, tex(uniyou9d.tfm) = %{tl_version}
Provides:       tex(uniyou9e.tfm) = %{tl_version}, tex(uniyou9f.tfm) = %{tl_version}
Provides:       tex(uniyoua0.tfm) = %{tl_version}, tex(uniyoua1.tfm) = %{tl_version}
Provides:       tex(uniyoua2.tfm) = %{tl_version}, tex(uniyoua3.tfm) = %{tl_version}
Provides:       tex(uniyoua4.tfm) = %{tl_version}, tex(uniyoua5.tfm) = %{tl_version}
Provides:       tex(uniyoua6.tfm) = %{tl_version}, tex(uniyoua7.tfm) = %{tl_version}
Provides:       tex(uniyoua8.tfm) = %{tl_version}, tex(uniyoua9.tfm) = %{tl_version}
Provides:       tex(uniyouaa.tfm) = %{tl_version}, tex(uniyouab.tfm) = %{tl_version}
Provides:       tex(uniyouac.tfm) = %{tl_version}, tex(uniyouad.tfm) = %{tl_version}
Provides:       tex(uniyouae.tfm) = %{tl_version}, tex(uniyouaf.tfm) = %{tl_version}
Provides:       tex(uniyoub0.tfm) = %{tl_version}, tex(uniyoub1.tfm) = %{tl_version}
Provides:       tex(uniyoub2.tfm) = %{tl_version}, tex(uniyoub3.tfm) = %{tl_version}
Provides:       tex(uniyoub4.tfm) = %{tl_version}, tex(uniyoub5.tfm) = %{tl_version}
Provides:       tex(uniyoub6.tfm) = %{tl_version}, tex(uniyoub7.tfm) = %{tl_version}
Provides:       tex(uniyoub8.tfm) = %{tl_version}, tex(uniyoub9.tfm) = %{tl_version}
Provides:       tex(uniyouba.tfm) = %{tl_version}, tex(uniyoubb.tfm) = %{tl_version}
Provides:       tex(uniyoubc.tfm) = %{tl_version}, tex(uniyoubd.tfm) = %{tl_version}
Provides:       tex(uniyoube.tfm) = %{tl_version}, tex(uniyoubf.tfm) = %{tl_version}
Provides:       tex(uniyouc0.tfm) = %{tl_version}, tex(uniyouc1.tfm) = %{tl_version}
Provides:       tex(uniyouc2.tfm) = %{tl_version}, tex(uniyouc3.tfm) = %{tl_version}
Provides:       tex(uniyouc4.tfm) = %{tl_version}, tex(uniyouc5.tfm) = %{tl_version}
Provides:       tex(uniyouc6.tfm) = %{tl_version}, tex(uniyouc7.tfm) = %{tl_version}
Provides:       tex(uniyouc8.tfm) = %{tl_version}, tex(uniyouc9.tfm) = %{tl_version}
Provides:       tex(uniyouca.tfm) = %{tl_version}, tex(uniyoucb.tfm) = %{tl_version}
Provides:       tex(uniyoucc.tfm) = %{tl_version}, tex(uniyoucd.tfm) = %{tl_version}
Provides:       tex(uniyouce.tfm) = %{tl_version}, tex(uniyoucf.tfm) = %{tl_version}
Provides:       tex(uniyoud0.tfm) = %{tl_version}, tex(uniyoud1.tfm) = %{tl_version}
Provides:       tex(uniyoud2.tfm) = %{tl_version}, tex(uniyoud3.tfm) = %{tl_version}
Provides:       tex(uniyoud4.tfm) = %{tl_version}, tex(uniyoud5.tfm) = %{tl_version}
Provides:       tex(uniyoud6.tfm) = %{tl_version}, tex(uniyoud7.tfm) = %{tl_version}
Provides:       tex(uniyoud8.tfm) = %{tl_version}, tex(uniyoud9.tfm) = %{tl_version}
Provides:       tex(uniyouda.tfm) = %{tl_version}, tex(uniyoudb.tfm) = %{tl_version}
Provides:       tex(uniyoudc.tfm) = %{tl_version}, tex(uniyoudd.tfm) = %{tl_version}
Provides:       tex(uniyoude.tfm) = %{tl_version}, tex(uniyoudf.tfm) = %{tl_version}
Provides:       tex(uniyoue0.tfm) = %{tl_version}, tex(uniyoue1.tfm) = %{tl_version}
Provides:       tex(uniyoue2.tfm) = %{tl_version}, tex(uniyoue3.tfm) = %{tl_version}
Provides:       tex(uniyoue4.tfm) = %{tl_version}, tex(uniyoue5.tfm) = %{tl_version}
Provides:       tex(uniyoue6.tfm) = %{tl_version}, tex(uniyoue7.tfm) = %{tl_version}
Provides:       tex(uniyoue8.tfm) = %{tl_version}, tex(uniyoue9.tfm) = %{tl_version}
Provides:       tex(uniyouea.tfm) = %{tl_version}, tex(uniyoueb.tfm) = %{tl_version}
Provides:       tex(uniyouec.tfm) = %{tl_version}, tex(uniyoued.tfm) = %{tl_version}
Provides:       tex(uniyouee.tfm) = %{tl_version}, tex(uniyouef.tfm) = %{tl_version}
Provides:       tex(uniyouf0.tfm) = %{tl_version}, tex(uniyouf1.tfm) = %{tl_version}
Provides:       tex(uniyouf2.tfm) = %{tl_version}, tex(uniyouf3.tfm) = %{tl_version}
Provides:       tex(uniyouf4.tfm) = %{tl_version}, tex(uniyouf5.tfm) = %{tl_version}
Provides:       tex(uniyouf6.tfm) = %{tl_version}, tex(uniyouf7.tfm) = %{tl_version}
Provides:       tex(uniyouf8.tfm) = %{tl_version}, tex(uniyouf9.tfm) = %{tl_version}
Provides:       tex(uniyoufa.tfm) = %{tl_version}, tex(uniyoufb.tfm) = %{tl_version}
Provides:       tex(uniyoufc.tfm) = %{tl_version}, tex(uniyoufd.tfm) = %{tl_version}
Provides:       tex(uniyoufe.tfm) = %{tl_version}, tex(uniyouff.tfm) = %{tl_version}
Provides:       tex(uniyousl00.tfm) = %{tl_version}, tex(uniyousl01.tfm) = %{tl_version}
Provides:       tex(uniyousl02.tfm) = %{tl_version}, tex(uniyousl03.tfm) = %{tl_version}
Provides:       tex(uniyousl04.tfm) = %{tl_version}, tex(uniyousl05.tfm) = %{tl_version}
Provides:       tex(uniyousl06.tfm) = %{tl_version}, tex(uniyousl07.tfm) = %{tl_version}
Provides:       tex(uniyousl08.tfm) = %{tl_version}, tex(uniyousl09.tfm) = %{tl_version}
Provides:       tex(uniyousl0a.tfm) = %{tl_version}, tex(uniyousl0b.tfm) = %{tl_version}
Provides:       tex(uniyousl0c.tfm) = %{tl_version}, tex(uniyousl0d.tfm) = %{tl_version}
Provides:       tex(uniyousl0e.tfm) = %{tl_version}, tex(uniyousl0f.tfm) = %{tl_version}
Provides:       tex(uniyousl10.tfm) = %{tl_version}, tex(uniyousl11.tfm) = %{tl_version}
Provides:       tex(uniyousl12.tfm) = %{tl_version}, tex(uniyousl13.tfm) = %{tl_version}
Provides:       tex(uniyousl14.tfm) = %{tl_version}, tex(uniyousl15.tfm) = %{tl_version}
Provides:       tex(uniyousl16.tfm) = %{tl_version}, tex(uniyousl17.tfm) = %{tl_version}
Provides:       tex(uniyousl18.tfm) = %{tl_version}, tex(uniyousl19.tfm) = %{tl_version}
Provides:       tex(uniyousl1a.tfm) = %{tl_version}, tex(uniyousl1b.tfm) = %{tl_version}
Provides:       tex(uniyousl1c.tfm) = %{tl_version}, tex(uniyousl1d.tfm) = %{tl_version}
Provides:       tex(uniyousl1e.tfm) = %{tl_version}, tex(uniyousl1f.tfm) = %{tl_version}
Provides:       tex(uniyousl20.tfm) = %{tl_version}, tex(uniyousl21.tfm) = %{tl_version}
Provides:       tex(uniyousl22.tfm) = %{tl_version}, tex(uniyousl23.tfm) = %{tl_version}
Provides:       tex(uniyousl24.tfm) = %{tl_version}, tex(uniyousl25.tfm) = %{tl_version}
Provides:       tex(uniyousl26.tfm) = %{tl_version}, tex(uniyousl27.tfm) = %{tl_version}
Provides:       tex(uniyousl28.tfm) = %{tl_version}, tex(uniyousl29.tfm) = %{tl_version}
Provides:       tex(uniyousl2a.tfm) = %{tl_version}, tex(uniyousl2b.tfm) = %{tl_version}
Provides:       tex(uniyousl2c.tfm) = %{tl_version}, tex(uniyousl2d.tfm) = %{tl_version}
Provides:       tex(uniyousl2e.tfm) = %{tl_version}, tex(uniyousl2f.tfm) = %{tl_version}
Provides:       tex(uniyousl30.tfm) = %{tl_version}, tex(uniyousl31.tfm) = %{tl_version}
Provides:       tex(uniyousl32.tfm) = %{tl_version}, tex(uniyousl33.tfm) = %{tl_version}
Provides:       tex(uniyousl34.tfm) = %{tl_version}, tex(uniyousl35.tfm) = %{tl_version}
Provides:       tex(uniyousl36.tfm) = %{tl_version}, tex(uniyousl37.tfm) = %{tl_version}
Provides:       tex(uniyousl38.tfm) = %{tl_version}, tex(uniyousl39.tfm) = %{tl_version}
Provides:       tex(uniyousl3a.tfm) = %{tl_version}, tex(uniyousl3b.tfm) = %{tl_version}
Provides:       tex(uniyousl3c.tfm) = %{tl_version}, tex(uniyousl3d.tfm) = %{tl_version}
Provides:       tex(uniyousl3e.tfm) = %{tl_version}, tex(uniyousl3f.tfm) = %{tl_version}
Provides:       tex(uniyousl40.tfm) = %{tl_version}, tex(uniyousl41.tfm) = %{tl_version}
Provides:       tex(uniyousl42.tfm) = %{tl_version}, tex(uniyousl43.tfm) = %{tl_version}
Provides:       tex(uniyousl44.tfm) = %{tl_version}, tex(uniyousl45.tfm) = %{tl_version}
Provides:       tex(uniyousl46.tfm) = %{tl_version}, tex(uniyousl47.tfm) = %{tl_version}
Provides:       tex(uniyousl48.tfm) = %{tl_version}, tex(uniyousl49.tfm) = %{tl_version}
Provides:       tex(uniyousl4a.tfm) = %{tl_version}, tex(uniyousl4b.tfm) = %{tl_version}
Provides:       tex(uniyousl4c.tfm) = %{tl_version}, tex(uniyousl4d.tfm) = %{tl_version}
Provides:       tex(uniyousl4e.tfm) = %{tl_version}, tex(uniyousl4f.tfm) = %{tl_version}
Provides:       tex(uniyousl50.tfm) = %{tl_version}, tex(uniyousl51.tfm) = %{tl_version}
Provides:       tex(uniyousl52.tfm) = %{tl_version}, tex(uniyousl53.tfm) = %{tl_version}
Provides:       tex(uniyousl54.tfm) = %{tl_version}, tex(uniyousl55.tfm) = %{tl_version}
Provides:       tex(uniyousl56.tfm) = %{tl_version}, tex(uniyousl57.tfm) = %{tl_version}
Provides:       tex(uniyousl58.tfm) = %{tl_version}, tex(uniyousl59.tfm) = %{tl_version}
Provides:       tex(uniyousl5a.tfm) = %{tl_version}, tex(uniyousl5b.tfm) = %{tl_version}
Provides:       tex(uniyousl5c.tfm) = %{tl_version}, tex(uniyousl5d.tfm) = %{tl_version}
Provides:       tex(uniyousl5e.tfm) = %{tl_version}, tex(uniyousl5f.tfm) = %{tl_version}
Provides:       tex(uniyousl60.tfm) = %{tl_version}, tex(uniyousl61.tfm) = %{tl_version}
Provides:       tex(uniyousl62.tfm) = %{tl_version}, tex(uniyousl63.tfm) = %{tl_version}
Provides:       tex(uniyousl64.tfm) = %{tl_version}, tex(uniyousl65.tfm) = %{tl_version}
Provides:       tex(uniyousl66.tfm) = %{tl_version}, tex(uniyousl67.tfm) = %{tl_version}
Provides:       tex(uniyousl68.tfm) = %{tl_version}, tex(uniyousl69.tfm) = %{tl_version}
Provides:       tex(uniyousl6a.tfm) = %{tl_version}, tex(uniyousl6b.tfm) = %{tl_version}
Provides:       tex(uniyousl6c.tfm) = %{tl_version}, tex(uniyousl6d.tfm) = %{tl_version}
Provides:       tex(uniyousl6e.tfm) = %{tl_version}, tex(uniyousl6f.tfm) = %{tl_version}
Provides:       tex(uniyousl70.tfm) = %{tl_version}, tex(uniyousl71.tfm) = %{tl_version}
Provides:       tex(uniyousl72.tfm) = %{tl_version}, tex(uniyousl73.tfm) = %{tl_version}
Provides:       tex(uniyousl74.tfm) = %{tl_version}, tex(uniyousl75.tfm) = %{tl_version}
Provides:       tex(uniyousl76.tfm) = %{tl_version}, tex(uniyousl77.tfm) = %{tl_version}
Provides:       tex(uniyousl78.tfm) = %{tl_version}, tex(uniyousl79.tfm) = %{tl_version}
Provides:       tex(uniyousl7a.tfm) = %{tl_version}, tex(uniyousl7b.tfm) = %{tl_version}
Provides:       tex(uniyousl7c.tfm) = %{tl_version}, tex(uniyousl7d.tfm) = %{tl_version}
Provides:       tex(uniyousl7e.tfm) = %{tl_version}, tex(uniyousl7f.tfm) = %{tl_version}
Provides:       tex(uniyousl80.tfm) = %{tl_version}, tex(uniyousl81.tfm) = %{tl_version}
Provides:       tex(uniyousl82.tfm) = %{tl_version}, tex(uniyousl83.tfm) = %{tl_version}
Provides:       tex(uniyousl84.tfm) = %{tl_version}, tex(uniyousl85.tfm) = %{tl_version}
Provides:       tex(uniyousl86.tfm) = %{tl_version}, tex(uniyousl87.tfm) = %{tl_version}
Provides:       tex(uniyousl88.tfm) = %{tl_version}, tex(uniyousl89.tfm) = %{tl_version}
Provides:       tex(uniyousl8a.tfm) = %{tl_version}, tex(uniyousl8b.tfm) = %{tl_version}
Provides:       tex(uniyousl8c.tfm) = %{tl_version}, tex(uniyousl8d.tfm) = %{tl_version}
Provides:       tex(uniyousl8e.tfm) = %{tl_version}, tex(uniyousl8f.tfm) = %{tl_version}
Provides:       tex(uniyousl90.tfm) = %{tl_version}, tex(uniyousl91.tfm) = %{tl_version}
Provides:       tex(uniyousl92.tfm) = %{tl_version}, tex(uniyousl93.tfm) = %{tl_version}
Provides:       tex(uniyousl94.tfm) = %{tl_version}, tex(uniyousl95.tfm) = %{tl_version}
Provides:       tex(uniyousl96.tfm) = %{tl_version}, tex(uniyousl97.tfm) = %{tl_version}
Provides:       tex(uniyousl98.tfm) = %{tl_version}, tex(uniyousl99.tfm) = %{tl_version}
Provides:       tex(uniyousl9a.tfm) = %{tl_version}, tex(uniyousl9b.tfm) = %{tl_version}
Provides:       tex(uniyousl9c.tfm) = %{tl_version}, tex(uniyousl9d.tfm) = %{tl_version}
Provides:       tex(uniyousl9e.tfm) = %{tl_version}, tex(uniyousl9f.tfm) = %{tl_version}
Provides:       tex(uniyousla0.tfm) = %{tl_version}, tex(uniyousla1.tfm) = %{tl_version}
Provides:       tex(uniyousla2.tfm) = %{tl_version}, tex(uniyousla3.tfm) = %{tl_version}
Provides:       tex(uniyousla4.tfm) = %{tl_version}, tex(uniyousla5.tfm) = %{tl_version}
Provides:       tex(uniyousla6.tfm) = %{tl_version}, tex(uniyousla7.tfm) = %{tl_version}
Provides:       tex(uniyousla8.tfm) = %{tl_version}, tex(uniyousla9.tfm) = %{tl_version}
Provides:       tex(uniyouslaa.tfm) = %{tl_version}, tex(uniyouslab.tfm) = %{tl_version}
Provides:       tex(uniyouslac.tfm) = %{tl_version}, tex(uniyouslad.tfm) = %{tl_version}
Provides:       tex(uniyouslae.tfm) = %{tl_version}, tex(uniyouslaf.tfm) = %{tl_version}
Provides:       tex(uniyouslb0.tfm) = %{tl_version}, tex(uniyouslb1.tfm) = %{tl_version}
Provides:       tex(uniyouslb2.tfm) = %{tl_version}, tex(uniyouslb3.tfm) = %{tl_version}
Provides:       tex(uniyouslb4.tfm) = %{tl_version}, tex(uniyouslb5.tfm) = %{tl_version}
Provides:       tex(uniyouslb6.tfm) = %{tl_version}, tex(uniyouslb7.tfm) = %{tl_version}
Provides:       tex(uniyouslb8.tfm) = %{tl_version}, tex(uniyouslb9.tfm) = %{tl_version}
Provides:       tex(uniyouslba.tfm) = %{tl_version}, tex(uniyouslbb.tfm) = %{tl_version}
Provides:       tex(uniyouslbc.tfm) = %{tl_version}, tex(uniyouslbd.tfm) = %{tl_version}
Provides:       tex(uniyouslbe.tfm) = %{tl_version}, tex(uniyouslbf.tfm) = %{tl_version}
Provides:       tex(uniyouslc0.tfm) = %{tl_version}, tex(uniyouslc1.tfm) = %{tl_version}
Provides:       tex(uniyouslc2.tfm) = %{tl_version}, tex(uniyouslc3.tfm) = %{tl_version}
Provides:       tex(uniyouslc4.tfm) = %{tl_version}, tex(uniyouslc5.tfm) = %{tl_version}
Provides:       tex(uniyouslc6.tfm) = %{tl_version}, tex(uniyouslc7.tfm) = %{tl_version}
Provides:       tex(uniyouslc8.tfm) = %{tl_version}, tex(uniyouslc9.tfm) = %{tl_version}
Provides:       tex(uniyouslca.tfm) = %{tl_version}, tex(uniyouslcb.tfm) = %{tl_version}
Provides:       tex(uniyouslcc.tfm) = %{tl_version}, tex(uniyouslcd.tfm) = %{tl_version}
Provides:       tex(uniyouslce.tfm) = %{tl_version}, tex(uniyouslcf.tfm) = %{tl_version}
Provides:       tex(uniyousld0.tfm) = %{tl_version}, tex(uniyousld1.tfm) = %{tl_version}
Provides:       tex(uniyousld2.tfm) = %{tl_version}, tex(uniyousld3.tfm) = %{tl_version}
Provides:       tex(uniyousld4.tfm) = %{tl_version}, tex(uniyousld5.tfm) = %{tl_version}
Provides:       tex(uniyousld6.tfm) = %{tl_version}, tex(uniyousld7.tfm) = %{tl_version}
Provides:       tex(uniyousld8.tfm) = %{tl_version}, tex(uniyousld9.tfm) = %{tl_version}
Provides:       tex(uniyouslda.tfm) = %{tl_version}, tex(uniyousldb.tfm) = %{tl_version}
Provides:       tex(uniyousldc.tfm) = %{tl_version}, tex(uniyousldd.tfm) = %{tl_version}
Provides:       tex(uniyouslde.tfm) = %{tl_version}, tex(uniyousldf.tfm) = %{tl_version}
Provides:       tex(uniyousle0.tfm) = %{tl_version}, tex(uniyousle1.tfm) = %{tl_version}
Provides:       tex(uniyousle2.tfm) = %{tl_version}, tex(uniyousle3.tfm) = %{tl_version}
Provides:       tex(uniyousle4.tfm) = %{tl_version}, tex(uniyousle5.tfm) = %{tl_version}
Provides:       tex(uniyousle6.tfm) = %{tl_version}, tex(uniyousle7.tfm) = %{tl_version}
Provides:       tex(uniyousle8.tfm) = %{tl_version}, tex(uniyousle9.tfm) = %{tl_version}
Provides:       tex(uniyouslea.tfm) = %{tl_version}, tex(uniyousleb.tfm) = %{tl_version}
Provides:       tex(uniyouslec.tfm) = %{tl_version}, tex(uniyousled.tfm) = %{tl_version}
Provides:       tex(uniyouslee.tfm) = %{tl_version}, tex(uniyouslef.tfm) = %{tl_version}
Provides:       tex(uniyouslf0.tfm) = %{tl_version}, tex(uniyouslf1.tfm) = %{tl_version}
Provides:       tex(uniyouslf2.tfm) = %{tl_version}, tex(uniyouslf3.tfm) = %{tl_version}
Provides:       tex(uniyouslf4.tfm) = %{tl_version}, tex(uniyouslf5.tfm) = %{tl_version}
Provides:       tex(uniyouslf6.tfm) = %{tl_version}, tex(uniyouslf7.tfm) = %{tl_version}
Provides:       tex(uniyouslf8.tfm) = %{tl_version}, tex(uniyouslf9.tfm) = %{tl_version}
Provides:       tex(uniyouslfa.tfm) = %{tl_version}, tex(uniyouslfb.tfm) = %{tl_version}
Provides:       tex(uniyouslfc.tfm) = %{tl_version}, tex(uniyouslfd.tfm) = %{tl_version}
Provides:       tex(uniyouslfe.tfm) = %{tl_version}, tex(uniyouslff.tfm) = %{tl_version}
Provides:       tex(zhwinfonts.tex) = %{tl_version}, tex(c19fs.fd) = %{tl_version}
Provides:       tex(c19hei.fd) = %{tl_version}, tex(c19kai.fd) = %{tl_version}
Provides:       tex(c19li.fd) = %{tl_version}, tex(c19you.fd) = %{tl_version}
Provides:       tex(c19zhfs.fd) = %{tl_version}, tex(c19zhhei.fd) = %{tl_version}
Provides:       tex(c19zhkai.fd) = %{tl_version}, tex(c19zhli.fd) = %{tl_version}
Provides:       tex(c19zhsong.fd) = %{tl_version}, tex(c19zhyou.fd) = %{tl_version}
Provides:       tex(c70fs.fd) = %{tl_version}, tex(c70hei.fd) = %{tl_version}
Provides:       tex(c70kai.fd) = %{tl_version}, tex(c70li.fd) = %{tl_version}
Provides:       tex(c70you.fd) = %{tl_version}, tex(c70zhfs.fd) = %{tl_version}
Provides:       tex(c70zhhei.fd) = %{tl_version}, tex(c70zhkai.fd) = %{tl_version}
Provides:       tex(c70zhli.fd) = %{tl_version}, tex(c70zhsong.fd) = %{tl_version}
Provides:       tex(c70zhyou.fd) = %{tl_version}

%description -n texlive-zhmetrics
These are metrics to use existing Chinese TrueType fonts in
workflows that use LaTeX & dvipdfmx, or pdfLaTeX. The fonts
themselves are not included in the package. Six font families
are supported: kai, song, lishu, fangsong, youyuan and hei. Two
encodings (GBK and UTF-8) are supported.

%package -n texlive-zhmetrics-doc
Summary:        Documentation for zhmetrics
Version:        svn22207.r206

Provides:       tex-zhmetrics-doc
AutoReqProv:    No

%description -n texlive-zhmetrics-doc
Documentation for zhmetrics

%package -n texlive-zhnumber
Provides:       tex-zhnumber = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Chinese representations of numbers
Version:        svn46478
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty)
Provides:       tex(zhnumber-big5.cfg) = %{tl_version}, tex(zhnumber-gbk.cfg) = %{tl_version}
Provides:       tex(zhnumber-utf8.cfg) = %{tl_version}, tex(zhnumber.sty) = %{tl_version}

%description -n texlive-zhnumber
The package provides commands to typeset Chinese
representations of numbers. The main difference between this
package and CJKnumb is that the commands provided are
expandable in the 'proper' way.

%package -n texlive-zhnumber-doc
Summary:        Documentation for zhnumber
Version:        svn46478
Provides:       tex-zhnumber-doc
AutoReqProv:    No

%description -n texlive-zhnumber-doc
Documentation for zhnumber

%package -n texlive-zhspacing
Provides:       tex-zhspacing = %{tl_version}
License:        LPPL
Summary:        Spacing for mixed CJK-English documents in XeTeX
Version:        svn41145

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontspec.sty), tex(ulem.sty)
Provides:       tex(t-zhspacing.tex) = %{tl_version}, tex(zhmath.sty) = %{tl_version}
Provides:       tex(zhsmyclass.sty) = %{tl_version}, tex(zhspacing.sty) = %{tl_version}
Provides:       tex(zhsusefulmacros.sty) = %{tl_version}
Provides:       tex(zhfont.sty) = %{tl_version}, tex(zhulem.sty) = %{tl_version}

%description -n texlive-zhspacing
The package manages spacing in a CJK document; between
consecutive Chinese letters, spaces are ignored, but a
consistent space is inserted between Chinese text and English
(or mathematics). The package may be used by any document
format under XeTeX.

%package -n texlive-zhspacing-doc
Summary:        Documentation for zhspacing
Version:        svn41145

Provides:       tex-zhspacing-doc
AutoReqProv:    No

%description -n texlive-zhspacing-doc
Documentation for zhspacing

%package -n texlive-xprintlen
Provides:       tex-xprintlen = %{tl_version}
License:        LPPL 1.3
Summary:        Print TeX lengths in a variety of units
Version:        svn35928.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp.sty)
Provides:       tex(xprintlen.sty) = %{tl_version}

%description -n texlive-xprintlen
The package defines a command, \printlen, to print TeX lengths
in a variety of units. It can handle all units supported by
TeX. The package requires that a reasonably up to date version
of the fp package be installed on you system.

%package -n texlive-xprintlen-doc
Summary:        Documentation for xprintlen
Version:        svn35928.1.0

Provides:       tex-xprintlen-doc
AutoReqProv:    No

%description -n texlive-xprintlen-doc
Documentation for xprintlen

%package -n texlive-xpunctuate
Provides:       tex-xpunctuate = %{tl_version}
License:        LPPL 1.2
Summary:        Process trailing punctuation which may be redundant
Version:        svn26641.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(xpunctuate.sty) = %{tl_version}

%description -n texlive-xpunctuate
The package provides commands that enable the user (or package
writer) to insert punctuation after the macro. The method is
similar to that of xspace, but goes further. The package
provides the commands \xperiod, \xcomma and \xperiodcomma,
which follow a similar procedure to that of \xspace, and insert
punctuation if and only if it is necessary.

%package -n texlive-xpunctuate-doc
Summary:        Documentation for xpunctuate
Version:        svn26641.1.0

Provides:       tex-xpunctuate-doc
AutoReqProv:    No

%description -n texlive-xpunctuate-doc
Documentation for xpunctuate

%package -n texlive-xstring
Provides:       tex-xstring = %{tl_version}
License:        LPPL
Summary:        String manipulation for (La)TeX
Version:        svn31900.1.7c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xstring.sty) = %{tl_version}, tex(xstring.tex) = %{tl_version}

%description -n texlive-xstring
The package provides macros for manipulating strings -- testing
a string's contents, extracting substrings, substitution of
substrings and providing numbers such as string length,
position of, or number of recurrences of, a substring. The
package works equally in Plain TeX and LaTeX (though e-TeX is
always required). The strings to be processed may contain
(expandable) macros.

%package -n texlive-xstring-doc
Summary:        Documentation for xstring
Version:        svn31900.1.7c

Provides:       tex-xstring-doc
AutoReqProv:    No

%description -n texlive-xstring-doc
Documentation for xstring

%package -n texlive-xtab
Provides:       tex-xtab = %{tl_version}
License:        LPPL
Summary:        Break tables across pages
Version:        svn23347.2.3f

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xtab.sty) = %{tl_version}

%description -n texlive-xtab
Xtab is an extended and somewhat improved version of
supertabular; its xtabular environment provides tables that
break across pages.

%package -n texlive-xtab-doc
Summary:        Documentation for xtab
Version:        svn23347.2.3f

Provides:       tex-xtab-doc
AutoReqProv:    No

%description -n texlive-xtab-doc
Documentation for xtab

%package -n texlive-xwatermark
Provides:       tex-xwatermark = %{tl_version}
License:        LPPL 1.3
Summary:        Graphics and text watermarks on selected pages
Version:        svn28090.1.5.2d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(catoptions.sty), tex(ltxkeys.sty)
Provides:       tex(xwatermark.sty) = %{tl_version}

%description -n texlive-xwatermark
The package extends the author's draftmark and the watermark
packages.

%package -n texlive-xwatermark-doc
Summary:        Documentation for xwatermark
Version:        svn28090.1.5.2d

Provides:       tex-xwatermark-doc
AutoReqProv:    No

%description -n texlive-xwatermark-doc
Documentation for xwatermark

%package -n texlive-xyling
Provides:       tex-xyling = %{tl_version}
License:        LPPL
Summary:        Draw syntactic trees, etc., for linguistics literature, using xy-pic
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xy.sty), tex(color.sty), tex(ifthen.sty)
Provides:       tex(xyling.sty) = %{tl_version}

%description -n texlive-xyling
The macros in this package model the construction of linguistic
tree structures as a genuinely graphical problem: they contain
two types of objects, BRANCHES and NODE LABELS, and these are
positioned relative to a GRID. It is essential that each of
these three elements is constructed independent of the other
two, and hence they can be modified without unwanted side
effects. The macros are based on the xy-pic package.

%package -n texlive-xyling-doc
Summary:        Documentation for xyling
Version:        svn15878.1.1

Provides:       tex-xyling-doc
AutoReqProv:    No

%description -n texlive-xyling-doc
Documentation for xyling

%package -n texlive-xytree
Provides:       tex-xytree = %{tl_version}
License:        LPPL
Summary:        Tree macros using XY-Pic
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xy.sty)
Provides:       tex(xytree.sty) = %{tl_version}

%description -n texlive-xytree
The package provides means to draw linguistic syntactic trees
with ease and to support hopefully sufficient functionalities,
that the linguist may need. The package (of course) depends on
the XY-Pic package.

%package -n texlive-xytree-doc
Summary:        Documentation for xytree
Version:        svn15878.1.5

Provides:       tex-xytree-doc
AutoReqProv:    No

%description -n texlive-xytree-doc
Documentation for xytree

%package -n texlive-yafoot
Provides:       tex-yafoot = %{tl_version}
License:        LPPL
Summary:        A bundle of miscellaneous footnote packages
Version:        svn19086.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dblfnote.sty) = %{tl_version}, tex(fnpos.sty) = %{tl_version}
Provides:       tex(pfnote.sty) = %{tl_version}

%description -n texlive-yafoot
Contains three packages: - pfnote to number footnotes per page;
- fnpos to control the position of footnotes; and - dblfnote to
make footnotes double-columned.

%package -n texlive-yafoot-doc
Summary:        Documentation for yafoot
Version:        svn19086.0

Provides:       tex-yafoot-doc
AutoReqProv:    No

%description -n texlive-yafoot-doc
Documentation for yafoot

%package -n texlive-yagusylo
Provides:       tex-yagusylo = %{tl_version}
License:        LPPL
Summary:        A symbol loader
Version:        svn29803.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xifthen.sty), tex(suffix.sty), tex(xargs.sty), tex(xcolor.sty)
Provides:       tex(yagusylo.cfg) = %{tl_version}, tex(yagusylo.sty) = %{tl_version}

%description -n texlive-yagusylo
The name is by way of being an acronym for "Yet Another Grand
Unified Symbols Loader"... The package allows the user to
access a symbol without loading the package that usually
provides it; this has the advantage of avoiding the name
clashes that so commonly trouble those who load symbol-
packages.

%package -n texlive-yagusylo-doc
Summary:        Documentation for yagusylo
Version:        svn29803.1.2

Provides:       tex-yagusylo-doc
AutoReqProv:    No

%description -n texlive-yagusylo-doc
Documentation for yagusylo

%package -n texlive-ydoc
Provides:       tex-ydoc = %{tl_version}
License:        LPPL 1.3
Summary:        Macros for documentation of LaTeX classes and packages
Version:        svn26202.0.6alpha

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(hyperref.sty), tex(needspace.sty), tex(xcolor.sty), tex(listings.sty)
Requires:       tex(shortvrb.sty), tex(etoolbox.sty), tex(xspace.sty), tex(url.sty)
Requires:       tex(float.sty), tex(svn-prov.sty), tex(newverbs.sty)
Provides:       tex(ydocincl.tex) = %{tl_version}, tex(ydocstrip.tex) = %{tl_version}
Provides:       tex(ydoc-code.sty) = %{tl_version}, tex(ydoc-desc.sty) = %{tl_version}
Provides:       tex(ydoc-doc.sty) = %{tl_version}, tex(ydoc-expl.sty) = %{tl_version}
Provides:       tex(ydoc.cfg) = %{tl_version}, tex(ydoc.cls) = %{tl_version}
Provides:       tex(ydoc.sty) = %{tl_version}

%description -n texlive-ydoc
The package provides macros and environments to document LaTeX
packages and classes. It is an (as yet unfinished) alternative
to the ltxdoc class and the doc or xdoc packages. The aim is to
provide a different layout and more modern styles (using the
xcolor, hyperref packages, etc.) This is an alpha release, and
should probably not (yet) be used with other packages, since
the implementation might change. Nevertheless, the author uses
it to document his own packages.

%package -n texlive-ydoc-doc
Summary:        Documentation for ydoc
Version:        svn26202.0.6alpha

Provides:       tex-ydoc-doc
AutoReqProv:    No

%description -n texlive-ydoc-doc
Documentation for ydoc

%package -n texlive-zed-csp
Provides:       tex-zed-csp = %{tl_version}
License:        Zed
Summary:        Typesetting Z and CSP format specifications
Version:        svn17258.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(zed-csp.sty) = %{tl_version}

%description -n texlive-zed-csp
The package supports real-time CSP and incorporates the
functionality of Spivey's original Z package, written for LaTeX
2.09.

%package -n texlive-zed-csp-doc
Summary:        Documentation for zed-csp
Version:        svn17258.0

Provides:       tex-zed-csp-doc
AutoReqProv:    No

%description -n texlive-zed-csp-doc
Documentation for zed-csp

%package -n texlive-ziffer
Provides:       tex-ziffer = %{tl_version}
License:        LPPL
Summary:        Conversion of punctuation in maths mode
Version:        svn32279.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ziffer.sty) = %{tl_version}

%description -n texlive-ziffer
The package modifies the behaviour of characters in maths mode
so that: '.' is used as a one-thousand separator (as is common
in Germany) ',' is used as a decimal separator (as is common in
Germany) '--' is represented with spacing as appropriate to
such constructs as '1.000,--'. These conversions may be
switched on and off.

%package -n texlive-ziffer-doc
Summary:        Documentation for ziffer
Version:        svn32279.2.1

Provides:       tex-ziffer-doc
AutoReqProv:    No

%description -n texlive-ziffer-doc
Documentation for ziffer

%package -n texlive-zwgetfdate
Provides:       tex-zwgetfdate = %{tl_version}
License:        LPPL 1.3
Summary:        Get package or file date
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(zwgetfdate.sty) = %{tl_version}

%description -n texlive-zwgetfdate
The package can fetch the date declaration of packages and
files used by a document, and then provide the information in
macros. The facilities provide a means of obtaining the date of
a package being documented; this is mainly of use when
doc/docstrip.

%package -n texlive-zwgetfdate-doc
Summary:        Documentation for zwgetfdate
Version:        svn15878.0

Provides:       tex-zwgetfdate-doc
AutoReqProv:    No

%description -n texlive-zwgetfdate-doc
Documentation for zwgetfdate

%package -n texlive-zwpagelayout
Provides:       tex-zwpagelayout = %{tl_version}
License:        LPPL
Summary:        Page layout and crop-marks
Version:        svn28846.1.4d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(ifxetex.sty), tex(kvoptions.sty), tex(color.sty)
Provides:       tex(zwpagelayout.sty) = %{tl_version}

%description -n texlive-zwpagelayout
This package was developed as a typographers' toolbox offering
important basic features for everyday work. It allows setting
the paper size and the page layout; it can print crop marks;
and it can reflect pages both horizontally and vertically. The
package facilities work with TeX (output via dvips or
(x)dvipdfm(x)), and with pdfTeX.

%package -n texlive-zwpagelayout-doc
Summary:        Documentation for zwpagelayout
Version:        svn28846.1.4d

Provides:       tex-zwpagelayout-doc
AutoReqProv:    No

%description -n texlive-zwpagelayout-doc
Documentation for zwpagelayout

%package -n texlive-xcjk2uni
Provides:       tex-xcjk2uni = %{tl_version}
License:        LPPL 1.3
Summary:        Convert CJK characters to Unicode, in pdfTeX
Version:        svn46496
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty)
Provides:       tex(xCJK2uni-UBg5plus.def) = %{tl_version}
Provides:       tex(xCJK2uni-UBig5.def) = %{tl_version}, tex(xCJK2uni-UGB.def) = %{tl_version}
Provides:       tex(xCJK2uni-UGBK.def) = %{tl_version}, tex(xCJK2uni-UJIS.def) = %{tl_version}
Provides:       tex(xCJK2uni-UKS.def) = %{tl_version}, tex(xCJK2uni-make.tex) = %{tl_version}
Provides:       tex(xCJK2uni-sfd.def) = %{tl_version}, tex(xCJK2uni.sty) = %{tl_version}

%description -n texlive-xcjk2uni
The package provides commands to convert CJK characters to
Unicode in non-UTF-8 encoding; it provides hooks to support
hyperref in producing correct bookmarks. The bundle also
provides /ToUnicode mapping file(s) for a CJK subfont; these
can be used with the cmap package, allowing searches of, and
cut-and-paste operations on a PDF file generated by pdfTeX..

%package -n texlive-xcjk2uni-doc
Summary:        Documentation for xcjk2uni
Version:        svn46496
Provides:       tex-xcjk2uni-doc
AutoReqProv:    No

%description -n texlive-xcjk2uni-doc
Documentation for xcjk2uni

%package -n texlive-zxjafbfont
Provides:       tex-zxjafbfont = %{tl_version}
License:        MIT
Summary:        Fallback CJK font support for xeCJK
Version:        svn28539.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xeCJK.sty)
Provides:       tex(zxjafbfont.sty) = %{tl_version}

%description -n texlive-zxjafbfont
zxjafbfont package

%package -n texlive-zxjafbfont-doc
Summary:        Documentation for zxjafbfont
Version:        svn28539.0.2

Provides:       tex-zxjafbfont-doc
AutoReqProv:    No

%description -n texlive-zxjafbfont-doc
Documentation for zxjafbfont

%package -n texlive-zxjatype
Provides:       tex-zxjatype = %{tl_version}
License:        MIT
Summary:        Standard conforming typesetting of Japanese, for XeLaTeX
Version:        svn47597
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(xeCJK.sty), tex(xparse.sty), tex(etoolbox.sty)
Provides:       tex(zxjatype.sty) = %{tl_version}

%description -n texlive-zxjatype
zxjatype package

%package -n texlive-zxjatype-doc
Summary:        Documentation for zxjatype
Version:        svn47597
Provides:       tex-zxjatype-doc
AutoReqProv:    No

%description -n texlive-zxjatype-doc
Documentation for zxjatype

%package -n texlive-zxjafont
Provides:       tex-zxjafont = %{tl_version}
License:        MIT
Summary:        Set up Japanese font families for XeLaTeX
Version:        svn47613
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(fontspec.sty), tex(keyval.sty)
Provides:       tex(zxjafont.sty) = %{tl_version}

%description -n texlive-zxjafont
zxjafont package

%package -n texlive-zxjafont-doc
Summary:        Documentation for zxjafont
Version:        svn47613
Provides:       tex-zxjafont-doc
AutoReqProv:    No

%description -n texlive-zxjafont-doc
Documentation for zxjafont

%package -n texlive-xcookybooky
Provides:       tex-xcookybooky = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset (potentially long) recipes
Version:        svn36435.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(graphicx.sty), tex(xcolor.sty), tex(ifsym.sty)
Requires:       tex(cookingsymbols.sty), tex(wrapfig.sty)
Requires:       tex(iflang.sty), tex(ifthen.sty), tex(xkeyval.sty), tex(lettrine.sty)
Requires:       tex(fancyhdr.sty), tex(units.sty), tex(eso-pic.sty), tex(picture.sty)
Requires:       tex(tabulary.sty), tex(framed.sty)
Provides:       tex(xcookybooky.cfg) = %{tl_version}, tex(xcookybooky.sty) = %{tl_version}

%description -n texlive-xcookybooky
The package enables the user to typeset recipes, which could be
greater than one page. Above the recipe text two (optional)
pictures can be displayed. Other features are recipe name,
energy content, portions, preparation and baking time, baking
temperatures, recipe source and of course preparation steps and
required ingredients. At the bottom you may insert an optional
hint. The package depends on the Emerald fonts.

%package -n texlive-xcookybooky-doc
Summary:        Documentation for xcookybooky
Version:        svn36435.1.5

Provides:       tex-xcookybooky-doc
AutoReqProv:    No

%description -n texlive-xcookybooky-doc
Documentation for xcookybooky

%package -n texlive-yathesis
Provides:       tex-yathesis = %{tl_version}
License:        LPPL 1.3
Summary:        yathesis provides a LaTeX class that aims to help to write a thesis following French rules
Version:        svn48172
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xpatch.sty), tex(xstring.sty), tex(xparse.sty), tex(letltxmacro.sty)
Requires:       tex(xifthen.sty), tex(zref.sty), tex(pgfopts.sty), tex(etoolbox.sty)
Requires:       tex(morewrites.sty), tex(filehook.sty), tex(hopatch.sty), tex(xkeyval.sty)
Requires:       tex(geometry.sty), tex(graphicx.sty), tex(environ.sty), tex(adjustbox.sty)
Requires:       tex(array.sty), tex(textcase.sty), tex(translator.sty), tex(fixltx2e.sty)
Requires:       tex(iftex.sty), tex(epigraph.sty), tex(tcolorbox.sty), tex(marvosym.sty)
Requires:       tex(setspace.sty), tex(shorttoc.sty), tex(tocvsec2.sty), tex(tocbibind.sty)
Requires:       tex(fncychap.sty), tex(titleps.sty), tex(nonumonpart.sty), tex(xcolor.sty)
Requires:       tex(datatool.sty), tex(ifdraft.sty), tex(draftwatermark.sty), tex(babel.sty)
Requires:       tex(iflang.sty), tex(datetime.sty), tex(hypcap.sty), tex(bookmark.sty)
Requires:       tex(glossaries-babel.sty)
Provides:       tex(yathesis-demo.sty) = %{tl_version}, tex(yathesis.cls) = %{tl_version}

%description -n texlive-yathesis
The bundle provides a LaTeX class that formats a thesis
following French rules.

%package -n texlive-yathesis-doc
Summary:        Documentation for yathesis
Version:        svn48172
Provides:       tex-yathesis-doc
AutoReqProv:    No

%description -n texlive-yathesis-doc
Documentation for yathesis

%package -n texlive-york-thesis
Provides:       tex-york-thesis = %{tl_version}
License:        LPPL 1.3
Summary:        A thesis class file for York University, Toronto
Version:        svn23348.3.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(makeidx.sty)
Provides:       tex(york-thesis.cls) = %{tl_version}

%description -n texlive-york-thesis
York Graduate Studies has again changed the requirements for
theses and dissertations. The established york-thesis class
file now implements the changes made in Spring 2005.

%package -n texlive-york-thesis-doc
Summary:        Documentation for york-thesis
Version:        svn23348.3.6

Provides:       tex-york-thesis-doc
AutoReqProv:    No

%description -n texlive-york-thesis-doc
Documentation for york-thesis

%package -n texlive-xymtex
Provides:       tex-xymtex = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting chemical structures
Version:        svn32182.5.06

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(hetarom.sty), tex(methylen.sty), tex(xcolor.sty), tex(epic.sty)
Requires:       tex(xymtx-pdf.sty), tex(tikz.sty), tex(pgfcore.sty), tex(pstricks.sty)
Requires:       tex(pst-coil.sty)
Provides:       tex(aliphat.sty) = %{tl_version}, tex(assurelatexmode.sty) = %{tl_version}
Provides:       tex(bondcolor.sty) = %{tl_version}, tex(carom.sty) = %{tl_version}
Provides:       tex(ccycle.sty) = %{tl_version}, tex(chemstr.sty) = %{tl_version}
Provides:       tex(fusering.sty) = %{tl_version}, tex(hcycle.sty) = %{tl_version}
Provides:       tex(hetarom.sty) = %{tl_version}, tex(hetaromh.sty) = %{tl_version}
Provides:       tex(lewisstruc.sty) = %{tl_version}, tex(locant.sty) = %{tl_version}
Provides:       tex(lowcycle.sty) = %{tl_version}, tex(methylen.sty) = %{tl_version}
Provides:       tex(polymers.sty) = %{tl_version}, tex(sizeredc.sty) = %{tl_version}
Provides:       tex(steroid.sty) = %{tl_version}, tex(xymtex.sty) = %{tl_version}
Provides:       tex(xymtexpdf.sty) = %{tl_version}, tex(xymtexps.sty) = %{tl_version}
Provides:       tex(assurechemist.sty) = %{tl_version}, tex(chemist.sty) = %{tl_version}
Provides:       tex(chemtimes.sty) = %{tl_version}, tex(chmst-pdf.sty) = %{tl_version}
Provides:       tex(xymtx-pdf.sty) = %{tl_version}, tex(chmst-ps.sty) = %{tl_version}
Provides:       tex(xymtx-ps.sty) = %{tl_version}

%description -n texlive-xymtex
XyMTeX is a set of packages for drawing a wide variety of
chemical structural formulas in a way that reflects their
structure. The package provides three output modes: 'LaTeX',
'PostScript' and 'PDF'. XyMTeX's commands have a systematic set
of arguments for specifying substituents and their positions,
endocyclic double bonds, and bond patterns. In some cases there
are additional arguments for specifying hetero-atoms on the
vertices of heterocycles. It is believed that this systematic
design allows XyMTeX to operate as a practical (device-
independent) tool for use with LaTeX.

%package -n texlive-xymtex-doc
Summary:        Documentation for xymtex
Version:        svn32182.5.06

Provides:       tex-xymtex-doc
AutoReqProv:    No

%description -n texlive-xymtex-doc
Documentation for xymtex

%package -n texlive-xypic-tut-pt-doc
Summary:        Documentation for xypic-tut-pt
Version:        svn15878.0

Provides:       tex-xypic-tut-pt-doc
AutoReqProv:    No

%description -n texlive-xypic-tut-pt-doc
Documentation for xypic-tut-pt

%package -n texlive-youngtab
Provides:       tex-youngtab = %{tl_version}
License:        LPPL
Summary:        Typeset Young-Tableaux
Version:        svn17635.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(youngtab.sty) = %{tl_version}

%description -n texlive-youngtab
A package for typesetting Young-Tableaux, mathematical symbols
for the representations of groups, providing two macros,
\yng(1) and \young(1) to generate the whole Young-Tableaux.

%package -n texlive-youngtab-doc
Summary:        Documentation for youngtab
Version:        svn17635.1.1

Provides:       tex-youngtab-doc
AutoReqProv:    No

%description -n texlive-youngtab-doc
Documentation for youngtab

%package -n texlive-xebaposter
Provides:       tex-xebaposter = %{tl_version}
License:        LPPL 1.3
Summary:        Creates beautiful scientific Persian/Latin posters using TikZ
Version:        svn42046
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(calc.sty), tex(xcolor.sty), tex(tikz.sty)
Requires:       tex(pgf.sty), tex(ifthen.sty), tex(fontenc.sty), tex(biditools.sty)
Provides:       tex(xebaposter.cls) = %{tl_version}

%description -n texlive-xebaposter
This package is designed for making beautiful scientific
Persian/Latin posters. It is a fork of baposter by Brian Amberg
and Reinhold Kainhofer available at http://www.brian-
amberg.de/uni/poster/. baposter's users should be able to
compile their poster using xebaposter (instead of baposter)
without any problem.

%package -n texlive-xebaposter-doc
Summary:        Documentation for xebaposter
Version:        svn42046
Provides:       tex-xebaposter-doc
AutoReqProv:    No

%description -n texlive-xebaposter-doc
Documentation for xebaposter

%package -n texlive-xecjk
Provides:       tex-xecjk = %{tl_version}
License:        LPPL 1.3
Summary:        Support for CJK documents in XeLaTeX
Version:        svn47519
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(listings.sty), tex(xtemplate.sty), tex(xparse.sty)
Requires:       tex(l3keys2e.sty), tex(fontspec.sty), tex(xeCJKfntef.sty), tex(ulem.sty)
Requires:       tex(environ.sty), tex(CJKfntef.sty), tex(xunicode.sty)
Provides:       tex(full-stop.map) = %{tl_version}, tex(fullwidth-stop.map) = %{tl_version}
Provides:       tex(han-simp.map) = %{tl_version}, tex(han-trad.map) = %{tl_version}
Provides:       tex(xeCJK-listings.sty) = %{tl_version}, tex(xeCJK.cfg) = %{tl_version}
Provides:       tex(xeCJK.sty) = %{tl_version}, tex(xeCJKfntef.sty) = %{tl_version}
Provides:       tex(xunicode-addon.sty) = %{tl_version}, tex(xunicode-extra.def) = %{tl_version}

%description -n texlive-xecjk
A LaTeX package for typesetting CJK documents in the way users
have become used to, in the CJK package. The package requires a
current version of xtemplate (and hence of the current LaTeX 3
development environment).

%package -n texlive-xecjk-doc
Summary:        Documentation for xecjk
Version:        svn47519
Provides:       tex-xecjk-doc
AutoReqProv:    No

%description -n texlive-xecjk-doc
Documentation for xecjk

%package -n texlive-xecolor
Provides:       tex-xecolor = %{tl_version}
License:        LPPL 1.3
Summary:        Support for color in XeLaTeX
Version:        svn29660.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontspec.sty), tex(iftex.sty)
Provides:       tex(xecolor.sty) = %{tl_version}

%description -n texlive-xecolor
This is a simple package which defines about 140 different
colours using XeTeX's colour feature. The colours can be used
in bidirectional texts without any problem.

%package -n texlive-xecolor-doc
Summary:        Documentation for xecolor
Version:        svn29660.0.1

Provides:       tex-xecolor-doc
AutoReqProv:    No

%description -n texlive-xecolor-doc
Documentation for xecolor

%package -n texlive-xecyr
Provides:       tex-xecyr = %{tl_version}
License:        LPPL
Summary:        Using Cyrillic languages in XeTeX
Version:        svn20221.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(misccorr.sty), tex(xltxtra.sty), tex(xunicode.sty)
Provides:       tex(xu-ruenhyph.tex) = %{tl_version}, tex(xecyr.sty) = %{tl_version}

%description -n texlive-xecyr
Helper tools for using Cyrillic languages with XeLaTeX and
babel.

%package -n texlive-xecyr-doc
Summary:        Documentation for xecyr
Version:        svn20221.1.1

Provides:       tex-xecyr-doc
AutoReqProv:    No

%description -n texlive-xecyr-doc
Documentation for xecyr

%package -n texlive-xeindex
Provides:       tex-xeindex = %{tl_version}
License:        LPPL
Summary:        Automatic index generation for XeLaTeX
Version:        svn35756.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(makeidx.sty), tex(xesearch.sty)
Provides:       tex(xeindex.sty) = %{tl_version}

%description -n texlive-xeindex
The package is based on XeSearch, and will automatically index
words or phrases in an XeLaTeX document. Words are declared in
a list, and every occurrence then creates an index entry whose
content can be fully specified beforehand.

%package -n texlive-xeindex-doc
Summary:        Documentation for xeindex
Version:        svn35756.0.3

Provides:       tex-xeindex-doc
AutoReqProv:    No

%description -n texlive-xeindex-doc
Documentation for xeindex

%package -n texlive-xepersian
Provides:       tex-xepersian = %{tl_version}
License:        LPPL 1.3
Summary:        Persian for LaTeX, using XeTeX
Version:        svn48396
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(ifxetex.sty), tex(multido.sty), tex(datetime.sty)
Requires:       tex(multicol.sty), tex(fancyhdr.sty), tex(fancybox.sty), tex(geometry.sty)
Requires:       tex(textpos.sty), tex(hyphenat.sty), tex(lastpage.sty), tex(setspace.sty)
Requires:       tex(ragged2e.sty), tex(pifont.sty), tex(fullpage.sty), tex(calc.sty)
Requires:       tex(verbatim.sty), tex(tabularx.sty), tex(fontspec.sty), tex(bidi.sty)
Provides:       tex(parsidigits.map) = %{tl_version}, tex(algorithm-xepersian.def) = %{tl_version}
Provides:       tex(algorithmic-xepersian.def) = %{tl_version}
Provides:       tex(amsart-xepersian.def) = %{tl_version}
Provides:       tex(amsbook-xepersian.def) = %{tl_version}
Provides:       tex(appendix-xepersian.def) = %{tl_version}
Provides:       tex(article-xepersian.def) = %{tl_version}
Provides:       tex(artikel1-xepersian.def) = %{tl_version}
Provides:       tex(artikel2-xepersian.def) = %{tl_version}
Provides:       tex(artikel3-xepersian.def) = %{tl_version}
Provides:       tex(backref-xepersian.def) = %{tl_version}
Provides:       tex(bidimoderncv-xepersian.def) = %{tl_version}
Provides:       tex(bidituftesidenote-xepersian.def) = %{tl_version}
Provides:       tex(boek-xepersian.def) = %{tl_version}, tex(boek3-xepersian.def) = %{tl_version}
Provides:       tex(book-xepersian.def) = %{tl_version}, tex(bookest-xepersian.def) = %{tl_version}
Provides:       tex(breqn-xepersian.def) = %{tl_version}
Provides:       tex(color-localise-xepersian.def) = %{tl_version}
Provides:       tex(enumerate-xepersian.def) = %{tl_version}
Provides:       tex(extarticle-xepersian.def) = %{tl_version}
Provides:       tex(extbook-xepersian.def) = %{tl_version}
Provides:       tex(extrafootnotefeatures-xepersian.def) = %{tl_version}
Provides:       tex(extreport-xepersian.def) = %{tl_version}
Provides:       tex(flowfram-xepersian.def) = %{tl_version}
Provides:       tex(footnote-xepersian.def) = %{tl_version}
Provides:       tex(framed-xepersian.def) = %{tl_version}
Provides:       tex(glossaries-xepersian.def) = %{tl_version}
Provides:       tex(hyperref-xepersian.def) = %{tl_version}
Provides:       tex(imsproc-xepersian.def) = %{tl_version}
Provides:       tex(kashida-xepersian.def) = %{tl_version}
Provides:       tex(latex-localise-commands-xepersian.def) = %{tl_version}
Provides:       tex(latex-localise-environments-xepersian.def) = %{tl_version}
Provides:       tex(latex-localise-messages-xepersian.def) = %{tl_version}
Provides:       tex(latex-localise-misc-xepersian.def) = %{tl_version}
Provides:       tex(listings-xepersian.def) = %{tl_version}
Provides:       tex(loadingorder-xepersian.def) = %{tl_version}
Provides:       tex(localise-xepersian.def) = %{tl_version}
Provides:       tex(memoir-xepersian.def) = %{tl_version}
Provides:       tex(minitoc-xepersian.def) = %{tl_version}
Provides:       tex(natbib-xepersian.def) = %{tl_version}
Provides:       tex(packages-localise-xepersian.def) = %{tl_version}
Provides:       tex(rapport1-xepersian.def) = %{tl_version}
Provides:       tex(rapport3-xepersian.def) = %{tl_version}
Provides:       tex(refrep-xepersian.def) = %{tl_version}
Provides:       tex(report-xepersian.def) = %{tl_version}
Provides:       tex(scrartcl-xepersian.def) = %{tl_version}
Provides:       tex(scrbook-xepersian.def) = %{tl_version}
Provides:       tex(scrreprt-xepersian.def) = %{tl_version}
Provides:       tex(tkz-linknodes-xepersian.def) = %{tl_version}
Provides:       tex(tocloft-xepersian.def) = %{tl_version}
Provides:       tex(xepersian-localise-commands-xepersian.def) = %{tl_version}
Provides:       tex(xepersian-localise-environments-xepersian.def) = %{tl_version}
Provides:       tex(xepersian-magazine.cls) = %{tl_version}
Provides:       tex(xepersian-mathsdigitspec.sty) = %{tl_version}
Provides:       tex(xepersian-multiplechoice.sty) = %{tl_version}
Provides:       tex(xepersian-persiancal.sty) = %{tl_version}
Provides:       tex(xepersian.sty) = %{tl_version}

%description -n texlive-xepersian
The package supports Persian typesetting.

%package -n texlive-xepersian-doc
Summary:        Documentation for xepersian
Version:        svn48396
Provides:       tex-xepersian-doc
AutoReqProv:    No

%description -n texlive-xepersian-doc
Documentation for xepersian

%package -n texlive-xesearch
Provides:       tex-xesearch = %{tl_version}
License:        LPPL
Summary:        A string finder for XeTeX
Version:        svn16041.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(t-xesearch.tex) = %{tl_version}, tex(xesearch.sty) = %{tl_version}

%description -n texlive-xesearch
The package finds strings (e.g. (parts of) words or phrases)
and manipulates them (apply any macro), thus turning each word
or phrase into a possible command. It is written in plain XeTeX
and should thus work with any format (it is known to work with
LaTeX and ConTeXt). The main application for the moment is
XeIndex, an automatic index for XeLaTeX, but examples are given
of simple use to check spelling, count words, and highlight
syntax of programming languages.

%package -n texlive-xesearch-doc
Summary:        Documentation for xesearch
Version:        svn16041.0

Provides:       tex-xesearch-doc
AutoReqProv:    No

%description -n texlive-xesearch-doc
Documentation for xesearch

%package -n texlive-xespotcolor
Provides:       tex-xespotcolor = %{tl_version}
License:        LPPL 1.3
Summary:        Spot colours support for XeLaTeX
Version:        svn40118

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(graphics.sty), tex(color.sty), tex(everypage.sty)
Provides:       tex(xespotcolor.sty) = %{tl_version}

%description -n texlive-xespotcolor
The package provides macros for using spot colours in LaTeX
documents. The package is a reimplementation of the spotcolor
package for use with XeLaTeX. As such, it has the same user
interface and the same capabilities.

%package -n texlive-xespotcolor-doc
Summary:        Documentation for xespotcolor
Version:        svn40118

Provides:       tex-xespotcolor-doc
AutoReqProv:    No

%description -n texlive-xespotcolor-doc
Documentation for xespotcolor

%package -n texlive-xetexref-doc
Summary:        Documentation for xetexref
Version:        svn45230
Provides:       tex-xetexref-doc
AutoReqProv:    No

%description -n texlive-xetexref-doc
Documentation for xetexref

%package -n texlive-xetex-itrans
Provides:       tex-xetex-itrans = %{tl_version}
License:        LPPL 1.3
Summary:        Itrans input maps for use with XeLaTeX
Version:        svn35088.4.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(brh-kan.map) = %{tl_version}, tex(itrans-dvn.map) = %{tl_version}
Provides:       tex(itrans-iast.map) = %{tl_version}, tex(itrans-kan.map) = %{tl_version}
Provides:       tex(itrans-sankan.map) = %{tl_version}, tex(itrans-santel.map) = %{tl_version}
Provides:       tex(itrans-sdvn.map) = %{tl_version}, tex(itrans-tamil.map) = %{tl_version}
Provides:       tex(itrans-tel.map) = %{tl_version}

%description -n texlive-xetex-itrans
The package provides maps for use with XeLaTeX with coding done
using itrans. Fontspec maps are provided for Devanagari
(Sanskrit), for Sanskrit in Kannada and for Kannada itself.

%package -n texlive-xetex-itrans-doc
Summary:        Documentation for xetex-itrans
Version:        svn35088.4.2

Provides:       tex-xetex-itrans-doc
AutoReqProv:    No

%description -n texlive-xetex-itrans-doc
Documentation for xetex-itrans

%package -n texlive-xetex-pstricks
Provides:       tex-xetex-pstricks = %{tl_version}
License:        Public Domain
Summary:        Running PStricks under XeTeX
Version:        svn17055.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-xetex-pstricks
The package provides an indirection scheme for XeTeX to use the
pstricks xdvipdfmx.cfg configuration file, so that XeTeX
documents will load it in preference to the standard
pstricks.con configuration file. With this configuration, many
PSTricks features can be used in xelatex or plain xetex
documents.

%package -n texlive-xetex-pstricks-doc
Summary:        Documentation for xetex-pstricks
Version:        svn17055.0

Provides:       tex-xetex-pstricks-doc
AutoReqProv:    No

%description -n texlive-xetex-pstricks-doc
Documentation for xetex-pstricks

%package -n texlive-xetex-tibetan
Provides:       tex-xetex-tibetan = %{tl_version}
License:        LPPL
Summary:        XeTeX input maps for Unicode Tibetan
Version:        svn28847.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(loctib.map) = %{tl_version}, tex(wylie.map) = %{tl_version}

%description -n texlive-xetex-tibetan
The package provides a map for use with Jonathan Kew's TECkit,
to translate Tibetan to Unicode (range 0F00-0FFF).

%package -n texlive-xetex-tibetan-doc
Summary:        Documentation for xetex-tibetan
Version:        svn28847.0.1

Provides:       tex-xetex-tibetan-doc
AutoReqProv:    No

%description -n texlive-xetex-tibetan-doc
Documentation for xetex-tibetan

%package -n texlive-xetexfontinfo
Provides:       tex-xetexfontinfo = %{tl_version}
License:        ASL 2.0
Summary:        Report font features in XeTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(aat-info.tex) = %{tl_version}, tex(opentype-info.tex) = %{tl_version}

%description -n texlive-xetexfontinfo
A pair of documents to reveal the font features supported by
fonts usable in XeTeX. Use OpenType-info.tex for OpenType
fonts, and AAT-info.tex for AAT fonts (Mac OS X only).

%package -n texlive-xetexfontinfo-doc
Summary:        Documentation for xetexfontinfo
Version:        svn15878.0

Provides:       tex-xetexfontinfo-doc
AutoReqProv:    No

%description -n texlive-xetexfontinfo-doc
Documentation for xetexfontinfo

%package -n texlive-xetexko
Provides:       tex-xetexko = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Korean with Xe(La)TeX
Version:        svn48378
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontspec.sty), tex(kolabels-utf.sty)
Requires:       tex(konames-utf.sty)
Provides:       tex(xetexko-font.sty) = %{tl_version}, tex(xetexko-hanging.sty) = %{tl_version}
Provides:       tex(xetexko-josa.sty) = %{tl_version}, tex(xetexko-space.sty) = %{tl_version}
Provides:       tex(xetexko-vertical.sty) = %{tl_version}
Provides:       tex(xetexko.sty) = %{tl_version}

%description -n texlive-xetexko
The package supports typesetting Korean documents (including
old Hangul texts), using XeTeX. It enhances the existing
support, in XeTeX, providing features that provide quality
typesetting.

%package -n texlive-xetexko-doc
Summary:        Documentation for xetexko
Version:        svn48378
Provides:       tex-xetexko-doc
AutoReqProv:    No

%description -n texlive-xetexko-doc
Documentation for xetexko

%package -n texlive-xevlna
Provides:       tex-xevlna = %{tl_version}
License:        LPPL 1.3
Summary:        Insert non-breakable spaces using XeTeX
Version:        svn43864
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(xevlna.sty) = %{tl_version}

%description -n texlive-xevlna
The package will directly insert nonbreakable spaces (in Czech,
vlna or vlnka), after nonsyllabic prepositions and single
letter conjuctions, while the document is being typeset. (The
macros recognised maths and verbatim by TeX means.) (Inserting
nonbreakable spaces by a preprocessor will probably never be
fully reliable, because user defined macros and environments
cannot reliably be recognised.) The package works both with
(Plain) XeTeX and with XeLaTeX.

%package -n texlive-xevlna-doc
Summary:        Documentation for xevlna
Version:        svn43864
Provides:       tex-xevlna-doc
AutoReqProv:    No

%description -n texlive-xevlna-doc
Documentation for xevlna

%package -n texlive-xgreek
Provides:       tex-xgreek = %{tl_version}
License:        LPPL 1.3
Summary:        XeLaTeX package for typesetting Greek language documents (beta release)
Version:        svn46662
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(xgreek.sty) = %{tl_version}

%description -n texlive-xgreek
This package has been designed so to allow people to typeset
Greek language documents using XeLaTeX. And it is released in
the hope that people will use it and spot errors, bugs,
features so to improve it. Practically, it provides all the
capabilities of the greek option of the babel package. The
package can be invoked with any of the following options:
monotonic (for typesetting modern monotonic Greek), polytonic
(for typesetting modern polytonic Greek), and ancient (for
typesetting ancient texts). The default option is monotonic.
The command \setlanguage{<lang>} to activate the hyphenation
patterns of the language <lang> This, however, can be done only
if the format file has not been built with the babel mechanism.

%package -n texlive-xgreek-doc
Summary:        Documentation for xgreek
Version:        svn46662
Provides:       tex-xgreek-doc
AutoReqProv:    No

%description -n texlive-xgreek-doc
Documentation for xgreek

%package -n texlive-yannisgr
Provides:       tex-yannisgr = %{tl_version}
License:        GPLv2+
Summary:        Greek fonts by Yannis Haralambous
Version:        svn22613.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mrgrbf10.tfm) = %{tl_version}, tex(mrgrrg10.tfm) = %{tl_version}
Provides:       tex(mrgrsl10.tfm) = %{tl_version}, tex(mrgrti10.tfm) = %{tl_version}
Provides:       tex(rgrbf10.tfm) = %{tl_version}, tex(rgrrg10.tfm) = %{tl_version}
Provides:       tex(rgrsc10.tfm) = %{tl_version}, tex(rgrsl10.tfm) = %{tl_version}
Provides:       tex(rgrti10.tfm) = %{tl_version}

%description -n texlive-yannisgr
A family of 7-bit fonts with a code table designed for setting
modern polytonic Greek. The fonts are provided as Metafont
source; macros to produce a Greek variant of Plain TeX
(including a hyphenation table adapted to the fonts' code
table) are provided.

%package -n texlive-yannisgr-doc
Summary:        Documentation for yannisgr
Version:        svn22613.0

Provides:       tex-yannisgr-doc
AutoReqProv:    No

%description -n texlive-yannisgr-doc
Documentation for yannisgr

%package -n texlive-xltxtra
Provides:       tex-xltxtra = %{tl_version}
License:        LPPL
Summary:        "Extras" for LaTeX users of XeTeX
Version:        svn39453

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-metalogo, tex(ifluatex.sty), tex(fontspec.sty), tex(ifxetex.sty)
Requires:       tex(realscripts.sty), tex(metalogo.sty)
Provides:       tex(xltxtra.sty) = %{tl_version}

%description -n texlive-xltxtra
The package loads the fixltx2e package from the LaTeX
distribution, and etex.sty from the e-TeX distribution. The
package then patches the \- (discretionary hyphen command) to
use the current hyphen character (which may be different from
than the default, which is the character at the ASCII hyphen
slot), and loads the realscripts to patch the \textsuperscript
command (from the LaTeX kernel) and the \textsubscript command
(from the fixltx2e package). The package is loaded by the
fontspec package, so that it should not ordinarily be necessary
to load it explicitly. The package relies on the metalogo
package for typesetting the XeTeX and XeLaTeX logos.

%package -n texlive-xltxtra-doc
Summary:        Documentation for xltxtra
Version:        svn39453

Provides:       tex-xltxtra-doc
AutoReqProv:    No
Requires:       tex-metalogo-doc

%description -n texlive-xltxtra-doc
Documentation for xltxtra

%package -n texlive-xunicode
Provides:       tex-xunicode = %{tl_version}
License:        LPPL 1.3
Summary:        Generate Unicode characters from accented glyphs
Version:        svn30466.0.981

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-tipa, tex(graphicx.sty), tex(t3enc.def)
Provides:       tex(xunicode.sty) = %{tl_version}

%description -n texlive-xunicode
The package supports XeTeX's (and other putative future similar
engines') need for Unicode characters, in a similar way to what
the fontenc does for 8-bit (and the like) fonts: convert accent-
glyph sequence to a single Unicode character for output. The
package also covers glyphs specified by packages (such as tipa)
which define many commands for single text glyphs.

%package -n texlive-xunicode-doc
Summary:        Documentation for xunicode
Version:        svn30466.0.981

Provides:       tex-xunicode-doc
AutoReqProv:    No
Requires:       tex-tipa-doc

%description -n texlive-xunicode-doc
Documentation for xunicode

%package -n texlive-xassoccnt-doc
Provides:       tex-xassoccnt-doc = %{tl_version}
License:        LPPL
Summary:        doc files of xassoccnt
Version:        svn47976
AutoReqProv:    No

%description -n texlive-xassoccnt-doc
Documentation for xassoccnt

%package -n texlive-xassoccnt
Provides:       tex-xassoccnt = %{tl_version}
License:        LPPL
Summary:        Associated counters stepping simultaneously
Version:        svn47976
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xassoccnt.sty) = %{tl_version}

%description -n texlive-xassoccnt
This package provides a way of associating counters to an
existing driver counter so that incrementing the driver counter
will increase its associated counters as well. This package can
be regarded as a supplement to the totcount package by
Vasileios Koutavas, but it can be used without it, too.
xassoccnt is a successor and a complete rewrite of the assoccnt
package by the same author. However, as of 2015/11/07, some
features of assoccnt are not (yet) contained in xassoccnt, so
that the older package cannot yet be regarded as obsolete.

%package -n texlive-xcntperchap-doc
Provides:       tex-xcntperchap-doc = %{tl_version}
License:        LPPL
Summary:        doc files of xcntperchap
Version:        svn46236
AutoReqProv:    No

%description -n texlive-xcntperchap-doc
Documentation for xcntperchap

%package -n texlive-xcntperchap
Provides:       tex-xcntperchap = %{tl_version}
License:        LPPL
Summary:        Track the number of subsections etc. that occur in a specified tracklevel
Version:        svn46236
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(xcntperchap.sty) = %{tl_version}

%description -n texlive-xcntperchap
This package is the successor of cntperchap and allows to
provide more tracklevels than just only one.

%package -n texlive-xduthesis-doc
Provides:       tex-xduthesis-doc = %{tl_version}
License:        LPPL
Summary:        doc files of xduthesis
Version:        svn39694

AutoReqProv:    No

%description -n texlive-xduthesis-doc
Documentation for xduthesis

%package -n texlive-xduthesis
Provides:       tex-xduthesis = %{tl_version}
License:        LPPL
Summary:        XeLaTeX template for writing Xidian University Thesis
Version:        svn39694

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xduthesis.cls) = %{tl_version}, tex(xduthesis.cfg) = %{tl_version}

%description -n texlive-xduthesis
This is a XeLaTeX template for writing theses to apply academic
degrees in Xidian University. The template is designed
according to the official requirements on typesetting theses.
The template currently supports all levels of degrees from
bachelor to doctor, including both academic master and
professional master. But it is not guaranteed that you will
pass the typesetting check and obtain your degree by using this
template.

%package -n texlive-xellipsis-doc
Provides:       tex-xellipsis-doc = %{tl_version}
License:        LPPL
Summary:        doc files of xellipsis
Version:        svn47546
AutoReqProv:    No

%description -n texlive-xellipsis-doc
Documentation for xellipsis

%package -n texlive-xellipsis
Provides:       tex-xellipsis = %{tl_version}
License:        LPPL
Summary:        Extremely configurable ellipses with formats for various style manuals
Version:        svn47546
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(xellipsis.sty) = %{tl_version}

%description -n texlive-xellipsis
The xellipsis package provides a system for configuring
(almomst) every possible aspect of ellipses, including
preceding and proceeding characters; the character itself;
distances before and after each of these; and number of
characters. It comes with both a compatibility option for
standard LaTeX \ldots as well as preset package options for the
Chicago Manual of Style (Turabian); the Bluebook; and MLA
guidelines.

%package -n texlive-xsavebox-doc
Provides:       tex-xsavebox-doc = %{tl_version}
License:        LPPL
Summary:        doc files of xsavebox
Version:        svn48171
AutoReqProv:    No

%description -n texlive-xsavebox-doc
Documentation for xsavebox

%package -n texlive-xsavebox
Provides:       tex-xsavebox = %{tl_version}
License:        LPPL
Summary:        Saveboxes for repeating content without code replication, based on PDF Form XObjects
Version:        svn48171
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(xsavebox.sty) = %{tl_version}

%description -n texlive-xsavebox
The package defines commands for saving content that can be
repeatedly placed into the document without replicating DVI/PDF
code in the output file, allowing for smaller file size of the
final PDF and improved content caching for faster display in
certain PDF viewers. The method makes use of `Form XObjects'
defined in the PDF specification. The user commands are
modelled after the standard LaTeX commands \savebox, \sbox,
\usebox and the lrbox environment. All common TeX engines and
back-ends are supported: pdfLaTeX, LuaLaTeX LaTeX --> dvips -->
ps2pdf/Distiller (Xe)LaTeX --> (x)dvipdfmx

%package -n texlive-ycbook-doc
Provides:       tex-ycbook-doc = %{tl_version}
License:        LPPL
Summary:        doc files of ycbook
Version:        svn46201
AutoReqProv:    No

%description -n texlive-ycbook-doc
Documentation for ycbook

%package -n texlive-ycbook
Provides:       tex-ycbook = %{tl_version}
License:        LPPL
Summary:        A versatile book class
Version:        svn46201
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ycbook.cls) = %{tl_version}

%description -n texlive-ycbook
This class is intended to be an interpretation of the mwbk
class which is a part of the mwcls package. The mwcls classes
are simple, yet powerful and customizable classes that allow
the end-user to customize the layout of headers, headings etc.
They also have the benefit of being more economic in space than
the most common LaTeX classes, while keeping a clear appearance
and a smooth flow.

%package -n texlive-yinit-otf-doc
Provides:       tex-yinit-otf-doc = %{tl_version}
License:        Public Domain
Summary:        doc files of yinit-otf
Version:        svn40207

AutoReqProv:    No

%description -n texlive-yinit-otf-doc
Documentation for yinit-otf

%package -n texlive-yinit-otf
Provides:       tex-yinit-otf = %{tl_version}
License:        Public Domain
Summary:        OTF conversion of Yannis Haralambous' Old German decorative initials
Version:        svn40207

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Yinit.otf) = %{tl_version}

%description -n texlive-yinit-otf
This package is a conversion of the yinit font into OTF.
Original Metafont files for yinit are in the yinit package.

%package -n texlive-zhmetrics-uptex-doc
Provides:       tex-zhmetrics-uptex-doc = %{tl_version}
License:        LPPL
Summary:        doc files of zhmetrics-uptex
Version:        svn40728

AutoReqProv:    No

%description -n texlive-zhmetrics-uptex-doc
Documentation for zhmetrics-uptex

%package -n texlive-zhmetrics-uptex
Provides:       tex-zhmetrics-uptex = %{tl_version}
License:        LPPL
Summary:        Chinese font metrics for upTeX
Version:        svn40728

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(upzhsans-v.vf) = %{tl_version}, tex(upzhserifb-h.vf) = %{tl_version}
Provides:       tex(upzhserifb-v.vf) = %{tl_version}, tex(upzhsansb-h.vf) = %{tl_version}
Provides:       tex(upzhmono-h.vf) = %{tl_version}, tex(upzhsans-h.vf) = %{tl_version}
Provides:       tex(upzhmono-v.vf) = %{tl_version}, tex(upzhserifit-v.vf) = %{tl_version}
Provides:       tex(upzhserif-h.vf) = %{tl_version}, tex(upzhserifit-h.vf) = %{tl_version}
Provides:       tex(upzhsansb-v.vf) = %{tl_version}, tex(upzhserif-v.vf) = %{tl_version}
Provides:       tex(upzhsansb-v.tfm) = %{tl_version}, tex(upsansb-v.tfm) = %{tl_version}
Provides:       tex(upmono-h.tfm) = %{tl_version}, tex(upzhserif-v.tfm) = %{tl_version}
Provides:       tex(upzhserifb-v.tfm) = %{tl_version}, tex(upzhserifit-v.tfm) = %{tl_version}
Provides:       tex(upmono-v.tfm) = %{tl_version}, tex(upzhmono-h.tfm) = %{tl_version}
Provides:       tex(upsans-v.tfm) = %{tl_version}, tex(upzhserif-h.tfm) = %{tl_version}
Provides:       tex(upzhserifb-h.tfm) = %{tl_version}, tex(upzhsans-v.tfm) = %{tl_version}
Provides:       tex(upzhserifit-h.tfm) = %{tl_version}, tex(upserifit-v.tfm) = %{tl_version}
Provides:       tex(upsansb-h.tfm) = %{tl_version}, tex(upzhmono-v.tfm) = %{tl_version}
Provides:       tex(upsans-h.tfm) = %{tl_version}, tex(upserif-h.tfm) = %{tl_version}
Provides:       tex(upzhsans-h.tfm) = %{tl_version}, tex(upserif-v.tfm) = %{tl_version}
Provides:       tex(upserifb-h.tfm) = %{tl_version}, tex(upzhsansb-h.tfm) = %{tl_version}
Provides:       tex(upserifit-h.tfm) = %{tl_version}, tex(upserifb-v.tfm) = %{tl_version}

%description -n texlive-zhmetrics-uptex
The package contains some Chinese font metrics (JFM, VF, etc)
for upTeX engine, together with a simple DVIPDFMx font mapping
of Fandol fonts for DVIPDFMx.

%package -n texlive-xfakebold
Summary:        Fake a regular font for bold characters
Version:        svn48460
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(ifluatex.sty)
Requires:       tex(ifxetex.sty), tex(xkeyval.sty)
Provides:       tex(xfakebold.sty) = %{tl_version}

%description -n texlive-xfakebold
This package uses PDF's text rendering to modify the linewidth
of an outline font to get bold characters. It works only for
vectorfonts where the glyphs are defined by their outline. The
package works both in text and in math mode, for pdfLaTeX as
well as for LuaLaTeX. The package depends on ifluatex, ifxetex,
and xkeyval.

%package -n texlive-xtuthesis
Summary:        XTU thesis template
Version:        svn47049
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(xtuformat.sty) = %{tl_version}

%description -n texlive-xtuthesis
The package provides a thesis template for the Xiangtan
University.

%package -n texlive-xurl
Summary:        Allow url break at any alphanumerical character
Version:        svn47904
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(xurl.sty) = %{tl_version}

%description -n texlive-xurl
Package xurl loads package url by default and defines possible
url breaks for all alphanumerical characters and = / . : * - ~
' " All arguments which are valid for url can be used. It will
be passed to package url. xurl itself has no special optional
argument. For more information read the documentation of
package url.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD

cd %{buildroot}%{_texdir}/texmf-dist/
patch -p0 < %{_sourcedir}/texlive-2017-xepersian-python.patch

install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/xcharter public/xits"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*
rm -f %{buildroot}%{_datadir}/texlive/tlpkg/tlpobj/xecyr.*

%files -n texlive-xkeyval
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/xkeyval/
%{_texdir}/texmf-dist/tex/latex/xkeyval/

%files -n texlive-xkeyval-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xkeyval/

%files -n texlive-xcolor
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/xcolor/
%{_texdir}/texmf-dist/tex/latex/xcolor/

%files -n texlive-xcolor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xcolor/

%files -n texlive-xcite
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xcite/

%files -n texlive-xcite-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xcite/

%files -n texlive-xetexconfig
%{_texdir}/texmf-dist/tex/xelatex/xetexconfig/

%files -n texlive-xcharter
%license other-free.txt
%{_datadir}/fonts/xcharter
%{_texdir}/texmf-dist/fonts/afm/public/xcharter/
%{_texdir}/texmf-dist/fonts/enc/dvips/xcharter/
%{_texdir}/texmf-dist/fonts/map/dvips/xcharter/
%{_texdir}/texmf-dist/fonts/opentype/public/xcharter/
%{_texdir}/texmf-dist/fonts/tfm/public/xcharter/
%{_texdir}/texmf-dist/fonts/type1/public/xcharter/
%{_texdir}/texmf-dist/fonts/vf/public/xcharter/
%{_texdir}/texmf-dist/tex/latex/xcharter/

%files -n texlive-xcharter-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/fonts/xcharter/

%files -n texlive-xits
%license ofl.txt
%{_datadir}/fonts/xits
%{_texdir}/texmf-dist/fonts/opentype/public/xits/

%files -n texlive-xits-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/xits/

%files -n texlive-yfonts
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/yfonts/

%files -n texlive-yfonts-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/yfonts/

%files -n texlive-yfonts-t1
%license lppl1.txt 
%{_texdir}/texmf-dist/dvips/yfonts-t1/
%{_texdir}/texmf-dist/fonts/afm/public/yfonts-t1/
%{_texdir}/texmf-dist/fonts/map/dvips/yfonts-t1/
%{_texdir}/texmf-dist/fonts/type1/public/yfonts-t1/

%files -n texlive-yfonts-t1-doc
%license lppl1.txt 
%{_texdir}/texmf-dist/doc/fonts/yfonts-t1/

%files -n texlive-yhmath
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/yhmath/
%{_texdir}/texmf-dist/fonts/source/public/yhmath/
%{_texdir}/texmf-dist/fonts/tfm/public/yhmath/
%{_texdir}/texmf-dist/fonts/type1/public/yhmath/
%{_texdir}/texmf-dist/fonts/vf/public/yhmath/
%{_texdir}/texmf-dist/tex/latex/yhmath/

%files -n texlive-yhmath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/yhmath/

%files -n texlive-ytableau
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/ytableau/

%files -n texlive-ytableau-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/ytableau/

%files -n texlive-zlmtt
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/zlmtt/

%files -n texlive-zlmtt-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/zlmtt/

%files -n texlive-zapfchan
%license gpl.txt
%{_texdir}/texmf-dist/dvips/zapfchan/
%{_texdir}/texmf-dist/fonts/afm/adobe/zapfchan/
%{_texdir}/texmf-dist/fonts/afm/urw/zapfchan/
%{_texdir}/texmf-dist/fonts/map/dvips/zapfchan/
%{_texdir}/texmf-dist/fonts/tfm/adobe/zapfchan/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/zapfchan/
%{_texdir}/texmf-dist/fonts/type1/urw/zapfchan/
%{_texdir}/texmf-dist/fonts/vf/adobe/zapfchan/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/zapfchan/
%{_texdir}/texmf-dist/tex/latex/zapfchan/

%files -n texlive-zapfding
%license gpl.txt
%{_texdir}/texmf-dist/dvips/zapfding/
%{_texdir}/texmf-dist/fonts/afm/adobe/zapfding/
%{_texdir}/texmf-dist/fonts/afm/urw/zapfding/
%{_texdir}/texmf-dist/fonts/map/dvips/zapfding/
%{_texdir}/texmf-dist/fonts/tfm/adobe/zapfding/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/zapfding/
%{_texdir}/texmf-dist/fonts/type1/urw/zapfding/
%{_texdir}/texmf-dist/tex/latex/zapfding/

%files -n texlive-xq
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/xq/
%{_texdir}/texmf-dist/fonts/tfm/public/xq/
%{_texdir}/texmf-dist/tex/latex/xq/

%files -n texlive-xq-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/xq/

%files -n texlive-xskak
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xskak/

%files -n texlive-xskak-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xskak/

%files -n texlive-xlop
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/xlop/

%files -n texlive-xlop-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/xlop/

%files -n texlive-yax
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/yax/

%files -n texlive-yax-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/yax/

%files -n texlive-xmltexconfig
%{_texdir}/texmf-dist/tex/xmltex/xmltexconfig/

%files -n texlive-xyling
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xyling/

%files -n texlive-xyling-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xyling/

%files -n texlive-xcjk2uni
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xcjk2uni/

%files -n texlive-xcjk2uni-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xcjk2uni/

%files -n texlive-zxjafont
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/zxjafont/

%files -n texlive-zxjafont-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/zxjafont/

%files -n texlive-xpinyin
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xpinyin/

%files -n texlive-xpinyin-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xpinyin/

%files -n texlive-zhmetrics
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/
%{_texdir}/texmf-dist/tex/generic/zhmetrics/
%{_texdir}/texmf-dist/tex/latex/zhmetrics/

%files -n texlive-zhmetrics-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/zhmetrics/

%files -n texlive-zhnumber
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/zhnumber/

%files -n texlive-zhnumber-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/zhnumber/

%files -n texlive-zhspacing
%license lppl1.txt
%{_texdir}/texmf-dist/tex/context/third/zhspacing/
%{_texdir}/texmf-dist/tex/generic/zhspacing/
%{_texdir}/texmf-dist/tex/xelatex/zhspacing/

%files -n texlive-zhspacing-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/zhspacing/

%files -n texlive-xetexref-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xetex/xetexref/

%files -n texlive-xgreek
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/xgreek/

%files -n texlive-xgreek-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xgreek/

%files -n texlive-yannisgr
%license gpl2.txt
%{_texdir}/texmf-dist/fonts/source/public/yannisgr/
%{_texdir}/texmf-dist/fonts/tfm/public/yannisgr/

%files -n texlive-yannisgr-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/yannisgr/

%files -n texlive-xetex-devanagari
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xetex-devanagari/

%files -n texlive-xetex-devanagari-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xetex/xetex-devanagari/

%files -n texlive-zxjafbfont
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/zxjafbfont/

%files -n texlive-zxjafbfont-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/zxjafbfont/

%files -n texlive-zxjatype
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/zxjatype/

%files -n texlive-zxjatype-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/zxjatype/

%files -n texlive-xypic-tut-pt-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/xypic-tut-pt/

%files -n texlive-xifthen
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xifthen/

%files -n texlive-xifthen-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xifthen/

%files -n texlive-xpicture
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xpicture/

%files -n texlive-xpicture-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xpicture/

%files -n texlive-xypic
%license gpl.txt
%{_texdir}/texmf-dist/dvips/xypic/
%{_texdir}/texmf-dist/fonts/afm/public/xypic/
%{_texdir}/texmf-dist/fonts/enc/dvips/xypic/
%{_texdir}/texmf-dist/fonts/map/dvips/xypic/
%{_texdir}/texmf-dist/fonts/source/public/xypic/
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/
%{_texdir}/texmf-dist/fonts/type1/public/xypic/
%{_texdir}/texmf-dist/tex/generic/xypic/

%files -n texlive-xypic-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/xypic/

%files -n texlive-xargs
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xargs/

%files -n texlive-xargs-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xargs/

%files -n texlive-xcolor-solarized
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xcolor-solarized/

%files -n texlive-xcolor-solarized-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xcolor-solarized/

%files -n texlive-xcomment
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/xcomment/

%files -n texlive-xcomment-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/xcomment/

%files -n texlive-xdoc
%license lppl1.txt
%{_texdir}/texmf-dist/makeindex/xdoc/
%{_texdir}/texmf-dist/tex/latex/xdoc/

%files -n texlive-xdoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xdoc/

%files -n texlive-xfor
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xfor/

%files -n texlive-xfor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xfor/

%files -n texlive-xhfill
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xhfill/

%files -n texlive-xhfill-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xhfill/

%files -n texlive-xint
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/xint/

%files -n texlive-xint-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/xint/

%files -n texlive-xmpincl
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/xmpincl/

%files -n texlive-xmpincl-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/xmpincl/

%files -n texlive-xnewcommand
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xnewcommand/

%files -n texlive-xnewcommand-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xnewcommand/

%files -n texlive-xoptarg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xoptarg/

%files -n texlive-xoptarg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xoptarg/

%files -n texlive-xpatch
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xpatch/

%files -n texlive-xpatch-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xpatch/

%files -n texlive-xpeek
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xpeek/

%files -n texlive-xpeek-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xpeek/

%files -n texlive-xprintlen
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xprintlen/

%files -n texlive-xprintlen-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xprintlen/

%files -n texlive-xpunctuate
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/xpunctuate/

%files -n texlive-xpunctuate-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/xpunctuate/

%files -n texlive-xstring
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/xstring/

%files -n texlive-xstring-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/xstring/

%files -n texlive-xtab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xtab/

%files -n texlive-xtab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xtab/

%files -n texlive-xwatermark
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xwatermark/

%files -n texlive-xwatermark-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xwatermark/

%files -n texlive-xytree
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xytree/

%files -n texlive-xytree-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xytree/

%files -n texlive-yafoot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/yafoot/

%files -n texlive-yafoot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/yafoot/

%files -n texlive-yagusylo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/yagusylo/

%files -n texlive-yagusylo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/yagusylo/

%files -n texlive-ydoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/ydoc/
%{_texdir}/texmf-dist/tex/latex/ydoc/

%files -n texlive-ydoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ydoc/

%files -n texlive-zed-csp
%{_texdir}/texmf-dist/tex/latex/zed-csp/

%files -n texlive-zed-csp-doc
%{_texdir}/texmf-dist/doc/latex/zed-csp/

%files -n texlive-ziffer
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ziffer/

%files -n texlive-ziffer-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ziffer/

%files -n texlive-zwgetfdate
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/zwgetfdate/

%files -n texlive-zwgetfdate-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/zwgetfdate/

%files -n texlive-zwpagelayout
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/zwpagelayout/

%files -n texlive-zwpagelayout-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/zwpagelayout/

%files -n texlive-xpiano
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xpiano/

%files -n texlive-xpiano-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xpiano/

%files -n texlive-xii-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/xii/

%files -n texlive-xcookybooky
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xcookybooky/

%files -n texlive-xcookybooky-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xcookybooky/

%files -n texlive-yathesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/yathesis/

%files -n texlive-yathesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/yathesis/

%files -n texlive-york-thesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/york-thesis/

%files -n texlive-york-thesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/york-thesis/

%files -n texlive-xymtex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xymtex/

%files -n texlive-xymtex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xymtex/

%files -n texlive-youngtab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/youngtab/

%files -n texlive-youngtab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/youngtab/

%files -n texlive-xebaposter
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xebaposter/

%files -n texlive-xebaposter-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xebaposter/

%files -n texlive-xecjk
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xecjk/
%{_texdir}/texmf-dist/tex/xelatex/xecjk/

%files -n texlive-xecjk-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xecjk/

%files -n texlive-xecolor
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/xecolor/

%files -n texlive-xecolor-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xecolor/

%files -n texlive-xecyr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/xecyr/
%{_texdir}/texmf-dist/tex/xelatex/xecyr/

%files -n texlive-xecyr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xelatex/xecyr/

%files -n texlive-xeindex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/xelatex/xeindex/

%files -n texlive-xeindex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xelatex/xeindex/

%files -n texlive-xepersian
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xepersian/
%{_texdir}/texmf-dist/tex/xelatex/xepersian/

%files -n texlive-xepersian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xepersian/

%files -n texlive-xesearch
%license lppl1.txt
%{_texdir}/texmf-dist/tex/xetex/xesearch/

%files -n texlive-xesearch-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xetex/xesearch/

%files -n texlive-xespotcolor
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/xespotcolor/

%files -n texlive-xespotcolor-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xespotcolor/

%files -n texlive-xetex-itrans
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xetex-itrans/

%files -n texlive-xetex-itrans-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xetex-itrans/

%files -n texlive-xetex-pstricks
%license pd.txt
%{_texdir}/texmf-dist/tex/xelatex/xetex-pstricks/
%{_texdir}/texmf-dist/tex/xetex/xetex-pstricks/

%files -n texlive-xetex-pstricks-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/xetex/xetex-pstricks/

%files -n texlive-xetex-tibetan
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xetex-tibetan/

%files -n texlive-xetex-tibetan-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xetex/xetex-tibetan/

%files -n texlive-xetexfontinfo
%license apache2.txt
%{_texdir}/texmf-dist/tex/xetex/xetexfontinfo/

%files -n texlive-xetexfontinfo-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/xetex/xetexfontinfo/

%files -n texlive-xetexko
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xetex/xetexko/

%files -n texlive-xetexko-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xetex/xetexko/

%files -n texlive-xevlna
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/xevlna/

%files -n texlive-xevlna-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xevlna/

%files -n texlive-xltxtra
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/xltxtra/

%files -n texlive-xltxtra-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/xltxtra/

%files -n texlive-xunicode
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/xunicode/

%files -n texlive-xunicode-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/xunicode/

%files -n texlive-xassoccnt-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xassoccnt/

%files -n texlive-xassoccnt
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xassoccnt/

%files -n texlive-xcntperchap-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xcntperchap/

%files -n texlive-xcntperchap
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xcntperchap/

%files -n texlive-xduthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xduthesis/

%files -n texlive-xduthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xduthesis/

%files -n texlive-xellipsis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xellipsis/

%files -n texlive-xellipsis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xellipsis/

%files -n texlive-xsavebox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/xsavebox/

%files -n texlive-xsavebox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/xsavebox/

%files -n texlive-ycbook-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ycbook/

%files -n texlive-ycbook
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ycbook/

%files -n texlive-yinit-otf-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/yinit-otf/

%files -n texlive-yinit-otf
%license pd.txt
%{_texdir}/texmf-dist/fonts/opentype/public/yinit-otf/

%files -n texlive-zhmetrics-uptex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/zhmetrics-uptex/

%files -n texlive-zhmetrics-uptex
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/tfm/public/zhmetrics-uptex/
%{_texdir}/texmf-dist/fonts/vf/public/zhmetrics-uptex/

%files -n texlive-xcolor-material
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/xcolor-material/
%{_texdir}/texmf-dist/tex/latex/xcolor-material/

%files -n texlive-xechangebar
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/xelatex/xechangebar/
%{_texdir}/texmf-dist/tex/xelatex/xechangebar/

%files -n texlive-xltabular
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/xltabular/
%{_texdir}/texmf-dist/tex/latex/xltabular/

%files -n texlive-xsim
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/xsim/
%{_texdir}/texmf-dist/tex/latex/xsim/

%files -n texlive-yaletter
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/yaletter/
%{_texdir}/texmf-dist/tex/latex/yaletter/

%files -n texlive-zebra-goodies
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/zebra-goodies/
%{_texdir}/texmf-dist/tex/latex/zebra-goodies/

%files -n texlive-zhlipsum
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/zhlipsum/
%{_texdir}/texmf-dist/tex/latex/zhlipsum/

%files -n texlive-xii-lat
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/plain/xii-lat/

%files -n texlive-xfakebold
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/xfakebold/
%doc %{_texdir}/texmf-dist/doc/latex/xfakebold/

%files -n texlive-xtuthesis
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/xtuthesis/
%doc %{_texdir}/texmf-dist/doc/latex/xtuthesis/

%files -n texlive-xurl
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/xurl/
%doc %{_texdir}/texmf-dist/doc/latex/xurl/

%changelog
* Tue Oct 26 2021 liyanan <liyanan32@huawei.com> - 8:2018-25
- Modify the name field

* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
