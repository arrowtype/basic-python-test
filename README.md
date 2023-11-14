# Basic Python Test

I’m having various Python errors that seem to point to some kind of a Python installation issue.

This repo is a simple test to see whether I can install a dependency and use it, and to record errors that may occur when I do.

## Test

Here’s a repo to serve as a simple reproduction case of [an issue I’m having with ColdType](https://github.com/coldtype/coldtype/issues/151#issuecomment-1806587692), which may boil down to a Python path issue.

Create and activate a virtual environment with:

```sh
python3 -m venv venv && source venv/bin/activate
```

Install requirements:

```sh
pip install -r requirements.txt
```

Run ColdType from example script:

```sh
coldtype src/coldtype-example.py
```

The error I am getting is this:

```sh
Traceback (most recent call last):
  File "/Users/stephennixon/type-repos/basic-python-test/venv/lib/python3.11/site-packages/coldtype/renderer/__init__.py", line 548, in _single_thread_render
    result = render.normalize_result(render.run(rp, self.state))
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/stephennixon/type-repos/basic-python-test/venv/lib/python3.11/site-packages/coldtype/renderable/animation.py", line 214, in run
    return super().run(render_pass, renderer_state, render_bg=render_bg)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/stephennixon/type-repos/basic-python-test/venv/lib/python3.11/site-packages/coldtype/renderable/renderable.py", line 348, in run
    res = render_pass.fn(*render_pass.args)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/folders/qx/2l9crthn3rb450m148nmpfb80000gn/T/coldtype__coldtype-example_s3xrswyr.py", line 16, in versioned_ƒVERSION
    __VERSION__["text"].upper(),
    ~~~~~~~~~~~^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

I am have the venv active, and I have ColdType 0.10.14 installed, which I’ve verified this with `pip show coldtype`. However, the ColdType creator said that these code line numbers don’t match up with ColdType 0.10.14, and suggested that it may be a Python path issue. I’ve had somewhat similar, strange Python issues in the recent past, so I think they may be right. This repo is made in part to share when I seek out help.

## Steps tried to fix the isssue

- I’ve removed and remade the venv, then reinstalled the dependency.
- I’ve restarted my computer.
- I’ve installed the latest stable Python, 3.12, from python.org.
- I repeated this test after each step, with the same result.
  
## Potentially relevant notes

- I’m on an M1 Mac, running Ventura
- I’ve tried this with Python 3.10 and 3.12
- I have ensured that I’m on ColdType 0.10.14
