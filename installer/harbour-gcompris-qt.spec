# -*- rpm-spec -*-
Summary:        gcompris-qt
Name:           harbour-gcompris-qt
Version:        0.23_1
Release:        1
License:        unknown
Group:          unknown
Url: https://www.gcompris.org


Buildarch: i486
Prefix: /usr

%define _rpmdir /home/mersdk/build_i486/_CPack_Packages/Linux/RPM
%define _rpmfilename gcompris-0.23-Linux.rpm
%define _unpackaged_files_terminate_build 0
%define _topdir /home/mersdk/build_i486/_CPack_Packages/Linux/RPM




%description
GCompris description

# This is a shortcutted spec file generated by CMake RPM generator
# we skip _install step because CPack does that for us.
# We do only save CPack installed tree in _prepr
# and then restore it in build.
%prep
mv $RPM_BUILD_ROOT "/home/mersdk/build_i486/_CPack_Packages/Linux/RPM/tmpBBroot"
echo $RPM_BUILD_ROOT

#p build

%install
if [ -e $RPM_BUILD_ROOT ];
then
  rm -rf $RPM_BUILD_ROOT
fi
mv "/home/mersdk/build_i486/_CPack_Packages/Linux/RPM/tmpBBroot" $RPM_BUILD_ROOT

# >> macros
%define _requires_exclude /bin/sh
# << macros

%clean

%files
%defattr(-,root,root,-)
%dir "/usr"
%dir "/usr/bin"
"/usr/bin/harbour-gcompris-qt"
%dir "/usr/share"
%dir "/usr/share/applications"
"/usr/share/applications/harbour-gcompris-qt.desktop"
%dir "/usr/share/icons"
%dir "/usr/share/icons/hicolor"
%dir "/usr/share/icons/hicolor/86x86"
%dir "/usr/share/icons/hicolor/86x86/apps"
"/usr/share/icons/hicolor/86x86/apps/harbour-gcompris-qt.png"
%dir "/usr/share/harbour-gcompris-qt"
%dir "/usr/share/harbour-gcompris-qt/translations"
%dir "/usr/share/harbour-gcompris-qt/rcc"
"/usr/share/harbour-gcompris-qt/rcc/align4.rcc"
"/usr/share/harbour-gcompris-qt/rcc/erase_2clic.rcc"
"/usr/share/harbour-gcompris-qt/rcc/penalty.rcc"
"/usr/share/harbour-gcompris-qt/rcc/instruments.rcc"
"/usr/share/harbour-gcompris-qt/rcc/mining.rcc"
"/usr/share/harbour-gcompris-qt/rcc/canal_lock.rcc"
"/usr/share/harbour-gcompris-qt/rcc/scalesboard_weight.rcc"
"/usr/share/harbour-gcompris-qt/rcc/magic-hat-plus.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/magic-hat-minus.rcc"
"/usr/share/harbour-gcompris-qt/rcc/clickanddraw.rcc"
"/usr/share/harbour-gcompris-qt/rcc/lightsoff.rcc"
"/usr/share/harbour-gcompris-qt/rcc/enumerate.rcc"
"/usr/share/harbour-gcompris-qt/rcc/money_cents.rcc"
"/usr/share/harbour-gcompris-qt/rcc/click_on_letter.rcc"
"/usr/share/harbour-gcompris-qt/rcc/maze.rcc"
"/usr/share/harbour-gcompris-qt/rcc/ballcatch.rcc"
"/usr/share/harbour-gcompris-qt/rcc/money.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-sound.rcc"
"/usr/share/harbour-gcompris-qt/rcc/advanced_colors.rcc"
"/usr/share/harbour-gcompris-qt/rcc/gnumch-multiples.rcc"
"/usr/share/harbour-gcompris-qt/rcc/gnumch-equality.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory.rcc"
"/usr/share/harbour-gcompris-qt/rcc/money_back.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-div-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-add-minus-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/gnumch-primes.rcc"
"/usr/share/harbour-gcompris-qt/rcc/clockgame.rcc"
"/usr/share/harbour-gcompris-qt/rcc/algebra_by.rcc"
"/usr/share/harbour-gcompris-qt/rcc/color_mix_light.rcc"
"/usr/share/harbour-gcompris-qt/rcc/algorithm.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-mult-div.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-add-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/imageid.rcc"
"/usr/share/harbour-gcompris-qt/rcc/redraw.rcc"
"/usr/share/harbour-gcompris-qt/rcc/smallnumbers.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-mult-div-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/mosaic.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-wordnumber.rcc"
"/usr/share/harbour-gcompris-qt/rcc/align4-2players.rcc"
"/usr/share/harbour-gcompris-qt/rcc/numbers-odd-even.rcc"
"/usr/share/harbour-gcompris-qt/rcc/fifteen.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-enumerate.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-add-minus-mult-div-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/colors.rcc"
"/usr/share/harbour-gcompris-qt/rcc/activities.rcc"
"/usr/share/harbour-gcompris-qt/rcc/reversecount.rcc"
"/usr/share/harbour-gcompris-qt/rcc/mazerelative.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-add-minus-mult-div.rcc"
"/usr/share/harbour-gcompris-qt/rcc/money_back_cents.rcc"
"/usr/share/harbour-gcompris-qt/rcc/algebra_minus.rcc"
"/usr/share/harbour-gcompris-qt/rcc/scalesboard.rcc"
"/usr/share/harbour-gcompris-qt/rcc/braille_alphabets.rcc"
"/usr/share/harbour-gcompris-qt/rcc/leftright.rcc"
"/usr/share/harbour-gcompris-qt/rcc/smallnumbers2.rcc"
"/usr/share/harbour-gcompris-qt/rcc/football.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-sound-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-div.rcc"
"/usr/share/harbour-gcompris-qt/rcc/guessnumber.rcc"
"/usr/share/harbour-gcompris-qt/rcc/gnumch-inequality.rcc"
"/usr/share/harbour-gcompris-qt/rcc/core.rcc"
"/usr/share/harbour-gcompris-qt/rcc/missing-letter.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-add-minus.rcc"
"/usr/share/harbour-gcompris-qt/rcc/color_mix.rcc"
"/usr/share/harbour-gcompris-qt/rcc/wordsgame.rcc"
"/usr/share/harbour-gcompris-qt/rcc/redraw_symmetrical.rcc"
"/usr/share/harbour-gcompris-qt/rcc/target.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-mult.rcc"
"/usr/share/harbour-gcompris-qt/rcc/menu.rcc"
"/usr/share/harbour-gcompris-qt/rcc/erase.rcc"
"/usr/share/harbour-gcompris-qt/rcc/drawnumber.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-add.rcc"
"/usr/share/harbour-gcompris-qt/rcc/erase_clic.rcc"
"/usr/share/harbour-gcompris-qt/rcc/click_on_letter_up.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-mult-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/sudoku.rcc"
"/usr/share/harbour-gcompris-qt/rcc/followline.rcc"
"/usr/share/harbour-gcompris-qt/rcc/hexagon.rcc"
"/usr/share/harbour-gcompris-qt/rcc/planegame.rcc"
"/usr/share/harbour-gcompris-qt/rcc/clickgame.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-minus-tux.rcc"
"/usr/share/harbour-gcompris-qt/rcc/gletters.rcc"
"/usr/share/harbour-gcompris-qt/rcc/alphabet-sequence.rcc"
"/usr/share/harbour-gcompris-qt/rcc/scalesboard_weight_avoirdupois.rcc"
"/usr/share/harbour-gcompris-qt/rcc/traffic.rcc"
"/usr/share/harbour-gcompris-qt/rcc/mazeinvisible.rcc"
"/usr/share/harbour-gcompris-qt/rcc/algebra_plus.rcc"
"/usr/share/harbour-gcompris-qt/rcc/gnumch-factors.rcc"
"/usr/share/harbour-gcompris-qt/rcc/memory-math-minus.rcc"




%changelog
* Sun Jul 4 2010 Erk <eric.noulard@gmail.com>
  Generated by CPack RPM (no Changelog file were provided)
