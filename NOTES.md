
Ansible fact cache is done per host with the inventory host name as the key for a
tree of values.  This will probably result in bad performance for leveldb since a
change in any value results in a complete rewrite of the entry for a host.


This method may not be useful for reducing ansible memory usage.

Ansible stores facts as a data structure and keys on the host name.  This
does not fit well with leveldb.


It does fit better with multiple json files, but I am not sure that it will save any memory usage.

My experiments show that it does not.

