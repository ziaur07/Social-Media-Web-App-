function calculateDaysBetweenDates(begin, end) {
    const oneDay = 24 * 60 * 60 * 1000;
    return Math.round(Math.abs((begin - end) / oneDay));
}
// Express server on port 3000
