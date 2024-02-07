## Advanced Collections

* `list` - Mutable sequence of values
* `tuple` - Fixed sequence of values
* `set` - Sequence of distinct values
* `dictionary` - Collection of key-value pairs

### Advanced Collections (import collections)

* `namedtuple` - Tuple with names fields
* `defaultdict` - Dictionary that supplies default values
* `counter`(Counter) - Counts distinct values
* `deque` - Double-ended list object

## Using `deque`

* Shorter for "double-ended queue";pronounced "deck"

```python
from collections import deque

d = deque('abcdefg')
```