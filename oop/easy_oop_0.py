Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File hw02_community\venv\lib\site-packages\django\urls\resolvers.py", line 586, in url_patterns
    iter(patterns)
TypeError: 'module' object is not iterable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\twsomt\AppData\Local\Programs\Python\Python37\lib\threading.py", line 926, in _bootstrap_inner
    self.run()
  File "C:\Users\twsomt\AppData\Local\Programs\Python\Python37\lib\threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\utils\autoreload.py", line 54, in wrapper
    fn(*args, **kwargs)
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\core\management\commands\runserver.py", line 117, in inner_run
    self.check(display_num_errors=True)
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\core\management\base.py", line 390, in check
    include_deployment_checks=include_deployment_checks,
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\core\management\base.py", line 377, in _run_checks
    return checks.run_checks(**kwargs)
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\core\checks\registry.py", line 72, in run_checks
    new_errors = check(app_configs=app_configs)
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\core\checks\urls.py", line 40, in check_url_namespaces_unique
    all_namespaces = _load_all_namespaces(resolver)
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\core\checks\urls.py", line 67, in _load_all_namespaces
    namespaces.extend(_load_all_namespaces(pattern, current))
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\core\checks\urls.py", line 57, in _load_all_namespaces
    url_patterns = getattr(resolver, 'url_patterns', [])
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\utils\functional.py", line 80, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "D:\Projects\hw02_community\venv\lib\site-packages\django\urls\resolvers.py", line 593, in url_patterns
    raise ImproperlyConfigured(msg.format(name=self.urlconf_name))
django.core.exceptions.ImproperlyConfigured: The included URLconf '<module 'users.urls' from 'D:\\Projects\\hw02_community\\yatube\\users\\urls.py'>' does not appear to have any patterns in it. If you see valid patterns in the file then the issue is probably caused by a circular import.