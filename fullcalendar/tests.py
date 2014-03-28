from django.test import TestCase
from .util import snake_to_camel_case, convert_field_names, calendar_options


class CamelCaseTest(TestCase):
    def test_one_word_variable(self):
        s = 'one'
        self.assertEqual(snake_to_camel_case(s), 'one')

    def test_two_word_variable(self):
        s = 'two_word'
        self.assertEqual(snake_to_camel_case(s), 'twoWord')

    def test_three_word_variable(self):
        s = 'three_word_variable'
        self.assertEqual(snake_to_camel_case(s), 'threeWordVariable')

    def test_startswith_one_underscore(self):
        s = '_one_under'
        self.assertEqual(snake_to_camel_case(s), '_oneUnder')

    def test_startswith_two_underscores(self):
        s = '__two_under'
        self.assertEqual(snake_to_camel_case(s), '__twoUnder')

    def test_starts_ends_with_one_underscore(self):
        s = '_one_under_'
        self.assertEqual(snake_to_camel_case(s), '_oneUnder_')
    
    def test_starts_ends_with_two_underscores(self):
        s = '__two_under__'
        self.assertEqual(snake_to_camel_case(s), '__twoUnder__')


class ConvertFieldNames(TestCase):
    def test_conversion(self):
        l = [{'start': '2013-11-27', 
             'end': '2013-11-29', 
             'all_day': 'true', 
             '__size__': 1, 
             '__to_string__': 'false'}]
        self.assertEqual(convert_field_names(l), [{'start': '2013-11-27', 'end': '2013-11-29', 'allDay': 'true', '__size__': 1, '__toString__': 'false'}])


class CalendarOptions(TestCase):
    def test_options_string(self):
        s = '{timeFormat: "H:mm", header: {left: "prev,next today", center: "title", right: "month,agendaWeek,agendaDay",}'        
        self.assertEqual(calendar_options('all_events/',s), '{events: "all_events/", timeFormat: "H:mm", header: {left: "prev,next today", center: "title", right: "month,agendaWeek,agendaDay",}')

    def test_options_string_with_whitespaces(self):
        s = '   {timeFormat: "H:mm", header: {left: "prev,next today", center: "title", right: "month,agendaWeek,agendaDay",}    '        
        self.assertEqual(calendar_options('all_events/',s), '{events: "all_events/", timeFormat: "H:mm", header: {left: "prev,next today", center: "title", right: "month,agendaWeek,agendaDay",}')

    def test_options_empty_string(self):
        s = ''        
        self.assertEqual(calendar_options('all_events/',s), '{events: "all_events/"}')
        