from stolos import testing_tools as tt
from stolos import get_NS


def setup_qb(func_name):
    return ((), dict(
        app1=tt.makepath(func_name, 'app1'),
        app2=tt.makepath(func_name, 'app2'),
        app3=tt.makepath(func_name, 'app3'),
        app4=tt.makepath(func_name, 'app4'),
        item1="{}-{}".format(func_name, 'a'),
        item2="{}-{}".format(func_name, 'b'),
        item3="{}-{}".format(func_name, 'c'),
        item4="{}-{}".format(func_name, 'd'),
        item5="{}-{}".format(func_name, 'e'),
        item6="{}-{}".format(func_name, 'f'),
    ))


with_setup = tt.with_setup_factory(
    (tt.setup_job_ids, setup_qb, ),
    (tt.teardown_queue_backend, ),
    (tt.post_setup_queue_backend,
     lambda: dict(qbcli=get_NS().queue_backend))
)


with_setup, setup_qb
