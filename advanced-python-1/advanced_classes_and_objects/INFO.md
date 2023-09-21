### Computed Attributes

| Method                                | Description                               | Trigger                          |
|---------------------------------------|-------------------------------------------|----------------------------------|
| `object.__getattribute__(self, attr)` | Called for all attribute access           | When accessing `object.attr`     |
| `object.__getattr__(self, attr)`      | Called when attribute not found in object | When `object.attr` doesn't exist |
| `object.__setattr__(self, attr, val)` | Called to set an attribute                | When setting `object.attr = val` |
| `object.__delattr__(self, attr)`      | Called to delete an attribute             | When using `del object.attr`     |
| `object.__dir__(self)`                | Called to list attributes                 | When using `dir(object)`         |

