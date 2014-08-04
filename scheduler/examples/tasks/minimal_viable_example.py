"""This example demonstrates what you need to do to incorporate a
pyspark application with the scheduler's pyspark plugin
"""


def main(elem, ns, **job_id_identifiers):
    """The scheduler's pyspark plugin will call this function
    to begin the application

    The function parameters may be one of these:

        def main(sc, ns, **job_id_identifiers):
        def main(textFile, ns, **job_id_identifiers):
        def main(elem, ns, **job_id_identifiers):

    `sc` - an instance of a spark context
    `textFile` - a pyspark RDD from a textFile, where the data loaded
        into the textFile RDD is determined by ns.read_fp
    `elem` - assume this application is a simple map operation that receives
        individual elements of an RDD.
    `ns` - an argparse.Namespace containing whatever argparse options you
        specified + the default ones provided by the pyspark plugin
    `job_id_identifiers` - a dictionary of extra keyword args that make up
        the job_id. (The job_id identifies what variation of work this
        application performs).

    * Note that `sc`, `textFile` and `elem` are mutually exclusive.  They
      identify which specific api your pyspark application will use.
    """
    # ... your code here.
    result = elem
    return result


# And don't forget you would need to add this to the tasks graph:

#   "test_scheduler/test_minimal": {
#     "job_type": "pyspark",
#     "pymodule": "scheduler.examples.pyspark_example"
#   }

#
# Then, to run it, there are two methods:
#

# 1. Queue a job in the task queue and then run the job
# 2. Manually run a job (not recommended except for testing)

# Option 1 looks like this:

#   ./bin/submit_task -a test_scheduler/test_minimal --job_id 20140501_1_test
#
#   python -m scheduler.runner --zookeeper_hosts localhost:2181
#     -a test_scheduler/test_minimal --write_fp /tmp/alex --read_fp ./README.md

# Option 2 is not recommended.  It looks like this:
#
#   python -m scheduler.runner --zookeeper_hosts localhost:2181
#     -a test_scheduler/test_minimal --write_fp /tmp/alex --read_fp ./README.md
#     --job_id 20140501_1_test
