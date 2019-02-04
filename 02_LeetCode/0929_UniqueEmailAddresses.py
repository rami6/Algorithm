"""
Problem description
 - https://leetcode.com/problems/unique-email-addresses/

Result
 - Runtime: 44 ms, faster than 99.33% of Python3 online submissions for Unique Email Addresses.
 - Memory Usage: 6.5 MB, less than 27.40% of Python3 online submissions for Unique Email Addresses.

"""


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        domain_dict = {}
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            if '+' in local:
                local = local[:local.index('+')]
            if domain not in domain_dict:
                domain_dict[domain] = [local]
            elif local not in domain_dict[domain]:
                domain_dict[domain].append(local)

        return sum(list(map(lambda x: len(x), domain_dict.values())))
