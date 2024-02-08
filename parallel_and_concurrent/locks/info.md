### Deadlock

* All processes and threads are unable to continue executing

### Reentrant Mutex

* Can be locked multiple times by the same thread
* Must be unlocked as many times as it was locked

### Common Terms

* Reentrant mutex
* Reentrant lock
* Recursive mutex
* Recursive lock

### Lock vs. RLock
------------------

* Lock can be released by a different thread than was used to acquire it
* RLock must be released by the same thread that acquired it
    * Must be released the same number of times it was acquired

### Try Lock

____________

* Non-blocking lock/acquire method for mutex
* If the mutex is available, lock it and return TRUE
* If the mutex is not available, immediately return FALSE