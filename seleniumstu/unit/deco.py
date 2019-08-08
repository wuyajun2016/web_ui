import functools
import unittest


def dependon(depend=None):
    """
    装饰器：
    表明依赖于那个用例，如果依赖的那个用例失败/错误/跳过，那么加了装饰器的用例也将跳过
    """
    def wraper_func(test_func):
        @functools.wraps(test_func)
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._resultForDoCleanups", self._resultForDoCleanups.__dict__)
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            test = unittest.skipIf(flag, '{} failed  or  error or skipped'.format(depend))(test_func)
            return test(self)

        return inner_func

    return wraper_func
