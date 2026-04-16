class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            # reduce the email to its "common form" by following the rules
            split_email = email.split('@')
            # add the common form to email_set
            local_name = split_email[0]
            domain_name = split_email[1]

            # normalize both names

            # local_name:
            # . should be removed
            # everything after and including + should be removed
            local_name = local_name.replace(".", "")
            index = local_name.find("+")
            if index != -1:
                local_name = local_name[:index]

            common_form_email = f"{local_name}@{domain_name}"
            email_set.add(common_form_email)
            

        # return the length of email_set
        return len(email_set)