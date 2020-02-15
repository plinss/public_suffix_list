#!/usr/bin/env python3
"""Unit test."""

import datetime

import public_suffix_list as list


TESTS = {
    # '' input.
    '': ('', '', ''),
    # Mixed case.
    'COM': ('', '', 'com'),
    'example.COM': ('', 'example', 'com'),
    'WwW.example.COM': ('www', 'example', 'com'),
    # Leading dot.
    '.com': ('', '', 'com'),
    '.example': ('', '', 'example'),
    '.example.com': ('', 'example', 'com'),
    '.example.example': ('', 'example', 'example'),
    '.www.example.example': ('www', 'example', 'example'),
    # Trailing dot.
    'com.': ('', '', 'com'),
    'example.': ('', '', 'example'),
    'example.com.': ('', 'example', 'com'),
    'example.example.': ('', 'example', 'example'),
    # Unlisted TLD.
    'example': ('', '', 'example'),
    'example.example': ('', 'example', 'example'),
    'b.example.example': ('b', 'example', 'example'),
    'a.b.example.example': ('a.b', 'example', 'example'),
    # TLD with only 1 rule.
    'biz': ('', '', 'biz'),
    'domain.biz': ('', 'domain', 'biz'),
    'b.domain.biz': ('b', 'domain', 'biz'),
    'a.b.domain.biz': ('a.b', 'domain', 'biz'),
    # TLD with some 2-level rules.
    'com': ('', '', 'com'),
    'example.com': ('', 'example', 'com'),
    'b.example.com': ('b', 'example', 'com'),
    'a.b.example.com': ('a.b', 'example', 'com'),
    'uk.com': ('', '', 'uk.com'),
    'example.uk.com': ('', 'example', 'uk.com'),
    'b.example.uk.com': ('b', 'example', 'uk.com'),
    'a.b.example.uk.com': ('a.b', 'example', 'uk.com'),
    'test.ac': ('', 'test', 'ac'),
    # TLD with only 1 (wildcard) rule.
    'bd': ('', '', 'bd'),
    'c.bd': ('', '', 'c.bd'),
    'b.c.bd': ('', 'b', 'c.bd'),
    'a.b.c.bd': ('a', 'b', 'c.bd'),
    # More complex TLD.
    'jp': ('', '', 'jp'),
    'test.jp': ('', 'test', 'jp'),
    'www.test.jp': ('www', 'test', 'jp'),
    'ac.jp': ('', '', 'ac.jp'),
    'test.ac.jp': ('', 'test', 'ac.jp'),
    'www.test.ac.jp': ('www', 'test', 'ac.jp'),
    'kyoto.jp': ('', '', 'kyoto.jp'),
    'test.kyoto.jp': ('', 'test', 'kyoto.jp'),
    'ide.kyoto.jp': ('', '', 'ide.kyoto.jp'),
    'b.ide.kyoto.jp': ('', 'b', 'ide.kyoto.jp'),
    'a.b.ide.kyoto.jp': ('a', 'b', 'ide.kyoto.jp'),
    'c.kobe.jp': ('', '', 'c.kobe.jp'),
    'b.c.kobe.jp': ('', 'b', 'c.kobe.jp'),
    'a.b.c.kobe.jp': ('a', 'b', 'c.kobe.jp'),
    'city.kobe.jp': ('', 'city', 'kobe.jp'),
    'www.city.kobe.jp': ('www', 'city', 'kobe.jp'),
    # TLD with a wildcard rule and exceptions.
    'ck': ('', '', 'ck'),
    'test.ck': ('', '', 'test.ck'),
    'b.test.ck': ('', 'b', 'test.ck'),
    'a.b.test.ck': ('a', 'b', 'test.ck'),
    'www.ck': ('', 'www', 'ck'),
    'www.www.ck': ('www', 'www', 'ck'),
    # US K12.
    'us': ('', '', 'us'),
    'test.us': ('', 'test', 'us'),
    'www.test.us': ('www', 'test', 'us'),
    'ak.us': ('', '', 'ak.us'),
    'test.ak.us': ('', 'test', 'ak.us'),
    'www.test.ak.us': ('www', 'test', 'ak.us'),
    'k12.ak.us': ('', '', 'k12.ak.us'),
    'test.k12.ak.us': ('', 'test', 'k12.ak.us'),
    'www.test.k12.ak.us': ('www', 'test', 'k12.ak.us'),
    # IDN labels.
    '食狮.com.cn': ('', '食狮', 'com.cn'),
    '食狮.公司.cn': ('', '食狮', '公司.cn'),
    'www.食狮.公司.cn': ('www', '食狮', '公司.cn'),
    'shishi.公司.cn': ('', 'shishi', '公司.cn'),
    '公司.cn': ('', '', '公司.cn'),
    '食狮.中国': ('', '食狮', '中国'),
    'www.食狮.中国': ('www', '食狮', '中国'),
    'shishi.中国': ('', 'shishi', '中国'),
    '中国': ('', '', '中国'),
    # Same as above, but punycoded.
    'xn--85x722f.com.cn': ('', 'xn--85x722f', 'com.cn'),
    'xn--85x722f.xn--55qx5d.cn': ('', 'xn--85x722f', 'xn--55qx5d.cn'),
    'www.xn--85x722f.xn--55qx5d.cn': ('www', 'xn--85x722f', 'xn--55qx5d.cn'),
    'shishi.xn--55qx5d.cn': ('', 'shishi', 'xn--55qx5d.cn'),
    'xn--55qx5d.cn': ('', '', 'xn--55qx5d.cn'),
    'xn--85x722f.xn--fiqs8s': ('', 'xn--85x722f', 'xn--fiqs8s'),
    'www.xn--85x722f.xn--fiqs8s': ('www', 'xn--85x722f', 'xn--fiqs8s'),
    'shishi.xn--fiqs8s': ('', 'shishi', 'xn--fiqs8s'),
    'xn--fiqs8s': ('', '', 'xn--fiqs8s'),
}


class Log:
    """Test logger."""

    def _print(self, *args) -> None:
        print(' '.join([str(arg) for arg in args]))

    def detail(self, *args) -> None:
        """Print details."""
        self._print(*args)

    def warning(self, *args) -> None:
        """Print warnings."""
        self._print('WARNING', *args)

    def error(self, *args) -> None:
        """Print errors."""
        self._print('ERROR', *args)


if __name__ == "__main__":
    list.setup(refresh_interval=datetime.timedelta(seconds=15), log=Log())

    fail_count = 0
    for domain, expected in TESTS.items():
        result = list.split_domain(domain)
        if (result == expected):
            print('  PASS:', domain, '->', result)
        else:
            print('* FAIL:', domain, '->', result, 'expected', expected)
            fail_count += 1

    exit(0 < fail_count)
