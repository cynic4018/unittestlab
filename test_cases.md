# unittestlab
Katapon Sinpunwong 6010545722
## borderline cases 
Such as a list with 0 or 1 elements. 

  * TestCountElement
      - test_empty_case
      - test_one_element_case
  * TestBinarySearch
      - test_empty_case
## typical cases
Such as a list with a few duplicates or no duplicates.

  * TestCountElement
      - test_no_duplicates_case
## impossible cases 
Cases where the method should not work.

  * TestCountElement
      - test_impossible_case
  * TestBinarySearch
      - test_find_not_found
      - test_element_is_none
      
## extreme cases
Such as a huge list

  * TestCountElement
      - test_huge_list_case
  * TestBinarySearch
      - test_huge_list_case
