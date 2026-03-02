Distributed File System (DFS) 🌐

A high-performance, scalable, and fault-tolerant Distributed File System (DFS)
designed to provide a unified view of files spread across multiple physical nodes.
This system allows clients to access remote data as if it were stored on their local machine.

🚀 OverviewIn

a traditional file system, data is bound to a single disk. This project implements a client-server architecture that abstracts physical storage into a Single Global Namespace.
Key FeaturesLocation Transparency: 
Access files by path (e.g., /data/docs/file.txt) without needing to know which server node holds the data.
Fault Tolerance: Automatic data replication across multiple nodes. If one node fails, the data remains accessible.
High Scalability:
Seamlessly add new storage nodes to the cluster without downtime.
Concurrency Control: Integrated file-locking mechanisms to prevent data corruption during simultaneous writes.

🏗️ System ArchitectureThe system 

consists of three primary components:Name Node (Metadata Server): Acts as the "brain."
It stores the directory tree and the mapping of file blocks to Data Nodes.Data Nodes (Storage): The "muscle." 
These nodes store the actual chunks of data and handle read/write requests.Client Library:
The interface used by applications to talk to the Name Node and Data Nodes.

🛠️ Comparison of Common DFSSystemBest

ForConsistency ModelNFSLocal Linux NetworksStrongHDFSBig Data / Batch ProcessingEventual/Write-onceCephObject, Block,
& File storageStrongGlusterFSCloud & Media StreamingScalability-focused

💻 Getting Started

prerequisitesPython
3.10+pip install -r requirements.
txtBasic UsageTo mount the distributed drive on a local client:Bash
