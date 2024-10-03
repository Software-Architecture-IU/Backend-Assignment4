### The following is the implementation of Pipes-and-filters pattern.

#### Architecture

```

           |        |    |        |    |     |    |            |
 Source -> | Resize | -> | Mirror | -> | BNW | -> | Distortion | -> Sink
           |        |    |        |    |     |    |            |
               (1)          (2)          (3)            (4)

```

#### What is the advantage of this approach over having everything in a single process?

This way we may significantly simplify implementation of the efficient data pipeline: one process serves single purpose,
prepares data in certain way and then passes to the next process.

If we had everything in a single process, we would have had to design a more complex multithreaded system to achieve the
same level of performance, empoying multiple CPU cores.

#### Project Structure

```

├── .github
│   ├── workflows
│   │   ├── build.yml       - configuration of the linter actions in the Github CI/CD  
├── src 
│   ├── filters             - folder with filters
│   │   ├── base.py         - | base class for all the filters
                              | itself is not a functional component
    
│   │   ├── bnw.py          - black & white filter
│   │   ├── distortion.py   - distortion filter
│   │   ├── dummy.py        - | identity filter, (that applies no 
                              | operations and returns what it gets)
        
│   │   ├── mirror.py       - mirror filter
│   │   └── resize.py       - resize filter
│   ├── main.py             - sets up and governs the entire pipeline
│   ├── sink.py             - output of the pipeline
│   └── source.py           - sorce of the data
└── README.md               - brief explanation of the project and its structure

```


