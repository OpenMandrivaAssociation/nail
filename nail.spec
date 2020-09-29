Summary:	A MIME capable implementation of the mailx command
Name:		nail
Version:	12.4
Release:	28
License:	BSD
Group:		Networking/Mail
Url:		http://heirloom.sourceforge.net/mailx.html
Source0:	http://prdownloads.sourceforge.net/heirloom/mailx-%{version}.tar.bz2
# (mpol) 11.25 set PAGER to less, Mandriva doesn't provide pg
Patch1:		nail-11.25-pager.patch
Patch2:		mailx-12.4-nostrip.diff
Patch3:		mailx-12.4-optflags.diff
Patch4:		nail_optopt.patch
# patch from Fedora to make it build with openssl
Patch5:		mailx-12.4-openssl.patch
# patches 6-9 fix security issues, including CVE-2004-2771
# http://openwall.com/lists/oss-security/2014/12/16/12
Patch6:		0001-outof-Introduce-expandaddr-flag.patch
Patch7:		0002-unpack-Disable-option-processing-for-email-addresses.patch
Patch8:		0003-fio.c-Unconditionally-require-wordexp-support.patch
Patch9:		0004-globname-Invoke-wordexp-with-WRDE_NOCMD.patch
Patch10:	nail-12.4-no-sslv2.patch
Patch11:	nail-2.4-openssl11.patch
BuildRequires:	pkgconfig(openssl)
Provides:	mailx = %{EVRD}
Obsoletes:	mailx < %{EVRD}

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
%setup -qn mailx-%{version}
%patch1 -p1 -b .pager~
%patch2 -p0 -b .nostrip~
%patch3 -p0 -b .optflags~
%patch4 -p1 -b .optopt~
%patch5 -p1 -b .openssl~
%patch6 -p1 -b .openssl11~

# (tpg) adapt to OpenSSL3
grep -rl "SSLv2_client_method" * | xargs sed -i 's/SSLv2_client_method/TLS_client_method/g'
grep -rl "SSLv3_client_method" * | xargs sed -i 's/SSLv3_client_method/TLS_client_method/g'

%build
%serverbuild
make SENDMAIL=/usr/lib/sendmail LDFLAGS="%{build_ldflags}"

%install
%make_install PREFIX=%{_prefix} UCBINSTALL=/usr/bin/install
install -d  %{buildroot}/bin
mv %{buildroot}%{_bindir}/mailx %{buildroot}/bin/mail
ln -sf ../../bin/mail %{buildroot}%{_bindir}/nail
ln -sf ../../bin/mail %{buildroot}%{_bindir}/mailx
ln -sf ../../bin/mail %{buildroot}%{_bindir}/Mail
ln -sf mailx.1 %{buildroot}%{_mandir}/man1/mail.1
ln -sf mailx.1 %{buildroot}%{_mandir}/man1/Mail.1
ln -sf mailx.1 %{buildroot}%{_mandir}/man1/nail.1

%files
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
