
Ansible fact cache is done per host with the inventory host name as the key for a
tree of values.  This will probably result in bad performance for leveldb since a
change in any value results in a complete rewrite of the entry for a host.


