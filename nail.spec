Summary:	A MIME capable implementation of the mailx command
Name:		nail
Version:	12.4
Release:	%mkrel 9
License:	BSD
Group:		Networking/Mail
URL:		http://heirloom.sourceforge.net/mailx.html
Source0:	http://prdownloads.sourceforge.net/heirloom/mailx-%{version}.tar.bz2
# (mpol) 11.25 set PAGER to less, Mandriva doesn't provide pg
Patch1:		nail-11.25-pager.patch
Patch2:		mailx-12.4-nostrip.diff
Patch3:		mailx-12.4-optflags.diff
Patch4:		nail_optopt.patch
# patch from Fedora to make it build with openssl
Patch5:		mailx-12.4-openssl.patch
BuildRequires:	openssl-devel
Provides:	mailx = %{version}-%{release}
Obsoletes:	mailx
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Nail is derived from Berkeley Mail and is intended to provide the
functionality of the POSIX.2 mailx command with additional support
for MIME, UTF-8, POP3/POP3s, IMAP, SMTP (SSL, TLS, AUTH), S/MIME,
Maildir, and more. It provides enhanced features for interactive use,
such as caching and disconnected operation for IMAP, message threading,
scoring, filtering, and Bayesian junk mail filter. It is also usable
as a mail batch language, both for sending and receiving mail.

Since version 12.0 Nail has been integrated into the Heirloom project,
renamed to Mailx.

%prep
%setup -q -n mailx-%{version}
%patch1 -p1 -b .pager
%patch2 -p0 -b .nostrip
%patch3 -p0 -b .optflags
%patch4 -p1 -b .optopt
%patch5 -p1 -b .openssl

%build
%serverbuild
make SENDMAIL=/usr/lib/sendmail LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

%makeinstall_std PREFIX=%{_prefix} UCBINSTALL=/usr/bin/install
install -d  %{buildroot}/bin
mv %{buildroot}%{_bindir}/mailx %{buildroot}/bin/mail
ln -sf ../../bin/mail %{buildroot}%{_bindir}/nail
ln -sf ../../bin/mail %{buildroot}%{_bindir}/mailx
ln -sf ../../bin/mail %{buildroot}%{_bindir}/Mail
ln -sf mailx.1 %{buildroot}%{_mandir}/man1/mail.1
ln -sf mailx.1 %{buildroot}%{_mandir}/man1/Mail.1
ln -sf mailx.1 %{buildroot}%{_mandir}/man1/nail.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS INSTALL README TODO ChangeLog
%config(noreplace) %{_sysconfdir}/nail.rc
/bin/mail
%{_bindir}/nail
%{_bindir}/mailx
%{_bindir}/Mail
%{_mandir}/man1/mailx.1.*
%{_mandir}/man1/Mail.1.*
%{_mandir}/man1/mail.1.*
%{_mandir}/man1/nail.1.*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 12.4-8mdv2011.0
+ Revision: 666535
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 12.4-7mdv2011.0
+ Revision: 607030
- try to fuix weid build error
- rebuild

* Thu Apr 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 12.4-6mdv2010.1
+ Revision: 532997
- add patch from Fedora to make it build with openssl-1.0.0

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 12.4-4mdv2010.1
+ Revision: 511594
- rebuilt against openssl-0.9.8m

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 12.4-3mdv2010.0
+ Revision: 450161
- fix build: nail is implementation its own getopt and use a global
  optopt variable which conflicts with glibc optopt, using static
  fixes that (from Arnaud Patard)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 12.4-2mdv2010.0
+ Revision: 426202
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 12.4-1mdv2009.1
+ Revision: 317115
- 12.4
- fhs fixes
- use %%optflags and %%ldflags
- don't strip the binary at install

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 12.3-4mdv2009.0
+ Revision: 223332
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 12.3-3mdv2008.1
+ Revision: 153273
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 12.3-1mdv2008.0
+ Revision: 55263
- spec file clean
- use parallel build and %%serverbuild
- new version


* Thu Jan 18 2007 Gustavo De Nardin <gustavodn@mandriva.com> 12.2-1mdv2007.0
+ Revision: 110448
- new version 12.2
- more generous description
- keep package name, but handle upstream rename (nail->mailx, since 12.0)

* Thu Jan 18 2007 Gustavo De Nardin <gustavodn@mandriva.com> 11.25-2mdv2007.1
+ Revision: 110391

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 11.25-2mdk
- rebuilt against openssl-0.9.8a

* Mon Aug 01 2005 Marcel Pol <mpol@mandriva.org> 11.25-1mdk
- 11.25
- P1: set PAGER to less, Mandriva doesn't provide pg (bug #16844)
- parallel make broken

* Tue Jul 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 11.24-1mdk
- New release 11.24

* Wed Jun 15 2005 Frederic Lepied <flepied@mandriva.com> 11.22-2mdk
- sendmail is in /usr/sbin

* Fri Jun 03 2005 Stew Benedict <sbendict@mandriva.com> 11.22-1mdk
- 11.22
- provide mailx symlink for LSB and additional symlinks to replace mailx
- provides/obsoletes mailx

* Tue Jun 01 2004 Marcel Pol <mpol@mandrake.org> 10.7-1mdk
- 10.7

