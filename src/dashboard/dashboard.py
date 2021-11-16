

from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/', methods=['GET', 'POST'])
def dashboard():
    """
        **dashboard**
    :return:
    """
    return render_template('index.html')


@dashboard_bp.route('/dash/messaging', methods=['GET', 'POST'])
def dash_messaging():
    """

    :return:
    """
    return render_template('dashboard/messaging.html')


@dashboard_bp.route('/dash/payroll', methods=['GET', 'POST'])
def dash_payroll():
    """

    :return:
    """
    return render_template('dashboard/payroll.html')


@dashboard_bp.route('/dash/rates', methods=['GET', 'POST'])
def dash_rates():
    """

    :return:
    """
    return render_template('dashboard/rates.html')


@dashboard_bp.route('/dash/payments', methods=['GET', 'POST'])
def dash_payments():
    """

    :return:
    """
    return render_template('dashboard/payments.html')


@dashboard_bp.route('/dash/schedules', methods=['GET', 'POST'])
def dash_schedules():
    """

    :return:
    """
    return render_template('dashboard/schedules.html')


@dashboard_bp.route('/dash/reports', methods=['GET', 'POST'])
def dash_reports():
    """

    :return:
    """
    return render_template('dashboard/reports.html')
