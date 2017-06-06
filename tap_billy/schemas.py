invoice = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string'
        },
        'organizationId': {
            'type': 'string'
        },
        'type': {
            'type': 'string'
        },
        'createdTime': {
            'type': 'string',
            'format': 'date-time'
        },
        'approvedTime': {
            'type': 'string',
            'format': 'date-time'
        },
        'contactId': {
            'type': 'string'
        },
        'attContactPerson': {
            'type': ['null', 'string']
        },
        'entryDate': {
            'type': 'string',
            'format': 'date'
        },
        'paymentTermsMode': {
            'type': 'string'
        },
        'paymentTermsDays': {
            'type': 'integer'
        },
        'dueDate': {
            'type': 'string',
            'format': 'date'
        },
        'state': {
            'type': 'string'
        },
        'sentState': {
            'type': 'string'
        },
        'invoiceNo': {
            'type': 'string'
        },
        'taxMode': {
            'type': 'string'
        },
        'amount': {
            'type': 'number'
        },
        'tax': {
            'type': 'number'
        },
        'currencyId': {
            'type': 'string'
        },
        'exchangeRate': {
            'type': 'number'
        },
        'balance': {
            'type': 'number'
        },
        'isPaid': {
            'type': 'boolean'
        },
        'creditedInvoiceId': {
            'type': ['null', 'string']

        },
        'recurringInvoiceId': {
            'type': ['null', 'string']

        },
        'orderNo': {
            'type': ['null', 'string']

        }


    }
}

invoice_test = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string'
        },
        'organizationId': {
            'type': 'string'
        },
        'contactId': {
            'type': 'string'
        },
        'createdTime': {
            'type': 'string',
            'format': 'date-time'
        },
        'associations': {
            'type': 'string',
            'format': 'date-time'
        },
        'contactId': {
            'type': 'string'
        },
        'attContactPerson': {
            'type': 'string'
        },
        'entryDate': {
            'type': 'string',
            'format': 'date'
        }
    }

}
