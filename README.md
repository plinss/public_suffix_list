# public_suffix_list

This is a module for querying the Public Suffix List to determine effective top level domains.

It provides APIs to split domain names into subdomains, registered, and public suffix parts.

Note this module does NOT include a copy of the public suffix list, 
it downloads the list, caches it, and periodically checks for updates automatically.

As such, internet connectivity is required. 
If the list is unable to be refreshed,
it will continue to run with the last cached version.

For applications that do not have internet connectivity, 
use an alternate package that includes a copy of the list,
or pre-populate the cache file through other means.
Note that without periodic updates the list will get out of date.

Cache updates happen on a thread so do not cause processing delays.

See https://publicsuffix.org/ for details about the list.

## API

The package provides the following functions which operate on a single, global list instance:

#### public_suffix_list.setup(url: str = None, cache_dir: str = None, refresh_interval: datetime.timedelta = None, log: Logger = None) -> PublicSuffixList: ...

Initialize the global list.
Only needs to be called if not using the default values.

Accepts an optional URL to download the list from, the default is: https://publicsuffix.org/list/public_suffix_list.dat

The list cache will be stored in a file 'public_suffix_list.dat' in the cache_dir, the default cache_dir is '.'.

The refresh_interval defaults to 24 hours.

An optional logger will receive debug and error messages.
If a logger is not provided, fatal errors will raise exceptions.


#### public_suffix_list.split_domain(domain_name: str) -> Tuple[str, str, str]: ...

Split a domain name into subdomain, registered name, and publix suffix.

Returns a Tuple of (subdomain, registered name, public suffix).

e.g. www.example.com -> (www, example, com)


#### public_suffix_list.public_suffix(domain_name: str) -> str: ...

Return public suffix of domain name.

e.g. www.example.com -> com


#### public_suffix_list.registered_name(domain_name: str) -> str: ...

Return registered name of domain name only.

e.g. www.example.com -> example


#### public_suffix_list.registered_domain_name(domain_name: str) -> str: ...

Return fully qualified registered domain name.

e.g. www.example.com -> example.com


#### public_suffix_list.split_registered_domain_name(domain_name: str) -> Tuple[str, str]: ...

Split a domain name into subdomain and fully qualified registered domain name.

e.g. www.example.com -> (www, example.com)


---

And the following class:

### public_suffix_list.PublicSuffixList

#### PublicSuffixList(url: str = None, cache_dir: str = None, refresh_interval: datetime.timedelta = None, log: Logger = None) -> None: ...

Instantiate a PublicSuffixList.

Accepts an optional URL to download the list from, the default is: https://publicsuffix.org/list/public_suffix_list.dat

The list cache will be stored in a file 'public_suffix_list.dat' in the cache_dir, the default cache_dir is '.'.

The refresh_interval defaults to 24 hours.

An optional logger will receive debug and error messages.
If a logger is not provided, fatal errors will raise exceptions.


#### PublicSuffixList.split_domain(self, domain_name: str) -> Tuple[str, str, str]: ...

Split a domain name into subdomain, registered name, and publix suffix.

Returns a Tuple of (subdomain, registered name, public suffix).

e.g. www.example.com -> (www, example, com)


#### PublicSuffixList.public_suffix(self, domain_name: str) -> str:

Return public suffix of domain name.

e.g. www.example.com -> com


#### PublicSuffixList.registered_name(self, domain_name: str) -> str:

Return registered name of domain name only.

e.g. www.example.com -> example


#### PublicSuffixList.registered_domain_name(self, domain_name: str) -> str:

Return registered domain name.

e.g. www.example.com -> example.com


#### PublicSuffixList.split_registered_domain_name(self, domain_name: str) -> Tuple[str, str]:

Split a domain name into subdomain and registered domain.

e.g. www.example.com -> (www, example.com)


---

### pubic_suffix_list.Logger(Protocol)

The protocol for the optional logger.

#### Logger.detail(self, *args) -> None: ...

Print detailed debug information.

Used when downloading the list.

#### Logger.warning(self, *args) -> None: ...

Print a non-fatal error.

Used when the list download fails.

#### Logger.error(self, *args) -> None: ...

Print a fatal error.

Used when the cache is unavailable and the list is unable to be downloaded or stored.


## Installation

Install with pip:

    pip install public-suffix-list