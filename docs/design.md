Software design specification
=============================

Data format
-----------
Each subject/topic/concept is stored as a Markdown file with a YAML header section.
Here is an example of what the source file for `python.md` would look like:

    ---
    links:
      - title: The Python package index website
        url: https://pypi.python.org/pypi
        notes: |
          These are extra lines that would normally go below the link URL
          via https://www.python.org/
          code https://github.com/python/cpython
      - title: Django web framework
        url: https://www.djangoproject.com/
        notes: |
          This is a useful framework for building websites
          and now this continues on the next line
    ---

    Python
    ======
    Python is a dynamic, interpreted programming language with many useful libraries
    and a strong community of programmers.

    Language features
    -----------------
    Yada yada
    ...



Presentation
------------
The root directory contains top-level subjects, which contain high-level topics,
which in turn contain subtopics, and concepts.

Q: Should we distinguish between subjects, topics, concepts?
    

