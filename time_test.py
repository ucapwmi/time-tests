from times import time_range, compute_overlap_time
def test_timeoverlap():
    #two time ranges that do not overlap
    large1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short1 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")

    #two time ranges that both contain several intervals each
    large2 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2,60)
    short2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",3,60)


    #two time ranges that end exactly at the same time when the other starts
    large3 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    short3 = time_range("2010-01-12 10:00:00", "2010-01-12 10:45:00")

    assert compute_overlap_time(large1,short1) == [("2010-01-12 10:30:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large2,short2) == [('2010-01-12 10:30:00', '2010-01-12 10:34:20'),
 ('2010-01-12 10:35:20', '2010-01-12 10:39:40'),
 ('2010-01-12 10:40:40', '2010-01-12 10:45:00'),
 ('2010-01-12 11:00:30', '2010-01-12 10:34:20'),
 ('2010-01-12 11:00:30', '2010-01-12 10:39:40'),
 ('2010-01-12 11:00:30', '2010-01-12 10:45:00')]
    assert compute_overlap_time(large3,short3) == [('2010-01-12 10:30:00', '2010-01-12 10:45:00')]

from pytest import raises
