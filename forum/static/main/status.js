statusForm = document.getElementById('status-form')
statusInput = document.getElementById('change-bio')
oldstatus = statusInput.value

statusForm.addEventListener('submit', () => {
    statusInput.blur()
})

statusInput.addEventListener('focusout', () => {
    if (statusInput.value != oldstatus) {
        statusForm.submit()
        oldstatus = statusInput.value
    }
})