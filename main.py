import plotly.graph_objects as go
from PyQt5 import QtCore, QtWidgets
from ui_interface import *
from ui_popup import *
from ui_loading import *
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import os
import sys
import random
import time
import datetime
from PySide2 import *
from sql import (fake_data, display_table, search_employee, avg_age, avg_salary, total_salary, update_employee,
                 avg_salary_per_position, employee_per_position, avg_age_per_position, get_top_n_by_field, delete_employee, create_employee_object, insert_data)


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return


# to change QwebEngine Background color
HTML = """<html>
                <head><meta charset="utf-8" /></head>
                <body>
                <style>

                    body{
                        background-color:#1f232a;
                        overflow: hidden; /* Hide scrollbars */
                    }

                </style>
        """

# start of Fake Data Generator methods


def generator(sql_list):
    for q in sql_list:
        yield q


def prepare_data_from_sql():
    fake_data()
    employee_list = display_table()
    news_list = display_table("News")
    employee_gen = generator(employee_list)
    news_gen = generator(news_list)
    return employee_gen, len(employee_list), news_gen, len(news_list), news_list

# end of Fake Data Generator methods


def _downloadRequested(item='a'):  # QWebEngineDownloadItem
    item.accept()


class LoadingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoadingWindow()
        self.ui.setupUi(self)
        # self.ui.popupCancelBtn.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.show()

    def progressUpdate(self, progress):
        self.ui.progressBar.setValue(progress)

    def textUpdate(self, text):
        self.ui.loadingLabel.setText(text)


class Popup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PopupWindow()
        self.ui.setupUi(self)
        self.ui.popupCancelBtn.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)


class MainWindow(QMainWindow):

    def fetch_data(self):
        self.avg_salary_per_pos = avg_salary_per_position()
        self.emp_per_pos = employee_per_position()
        self.avg_per_pos = avg_age_per_position()
        self.top_n_by_salaray = get_top_n_by_field()
        self.top_n_by_age = get_top_n_by_field(field="age")


    def __init__(self):

        QMainWindow.__init__(self)

        self.employees_generator, self.employees_number, self.news_generator, self.news_number, self.news_list = prepare_data_from_sql()
        self.fetch_data()
        self.isChanged = False
        self.saveFormat = 'png'
        self.theme = "white"



        screen = QApplication.screens()[0].size()
        self.setFixedWidth(screen.width() //  1.5)
        self.setFixedHeight(screen.height() //  1.1)

        # #
        Progress = 10
        LoadWin.progressUpdate(Progress)
        LoadWin.textUpdate("Initializing...")
        # time.sleep(1)

        #
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.previousClickedBtn = self.ui.dashboardBtn
        self.rowsToDelete = []
        self.ui.deleteSelectedRowsBtn.hide()
        self.ui.menuBtn.clicked.connect(lambda: self.handleSlideLeftMenu())
        self.ui.settingsBtn.clicked.connect(
            lambda: self.handleSlideCenterMenu(index=1, centerTitle="Settings"))
        self.ui.newsBtn.clicked.connect(
            lambda: self.handleSlideCenterMenu(index=2, centerTitle="News"))
        self.ui.helpBtn.clicked.connect(
            lambda: self.handleSlideCenterMenu(index=0, centerTitle="Help"))
        self.ui.closeCenterMenuBtn.clicked.connect(
            lambda: self.handleSlideCenterMenu(index=-1))
        self.ui.deleteSelectedRowsBtn.clicked.connect(
            lambda: self.display_delete_query_popup(del_value='multi'))
        self.ui.personnelBtn.clicked.connect(
            lambda: self.handleMainContent(index=0, btn=self.ui.personnelBtn))
        self.ui.dashboardBtn.clicked.connect(
            lambda: self.handleMainContent(index=1, btn=self.ui.dashboardBtn))
        self.ui.hireBtn.clicked.connect(
            lambda: self.handleMainContent(index=2, btn=self.ui.hireBtn))
        self.ui.reportBtn.clicked.connect(
            lambda: self.handleMainContent(index=3,  btn=self.ui.reportBtn))
        self.ui.closeRightMenuBtn.clicked.connect(
            lambda: self.handleSlideRightMenu(index=-1))
        self.ui.profileBtn.clicked.connect(
            lambda: self.handleSlideRightMenu(index=0))

        # Right Menu
        effect = QGraphicsDropShadowEffect(
            self.ui.rightMenuContainer, enabled=True, blurRadius=5)
        self.ui.profileAvatarLabel.setGraphicsEffect(effect)
        self.ui.rightMenuExitBtn.clicked.connect(self.close)

        # Center Menu
        self.ui.githubBtn.clicked.connect(lambda: self.open_webbrowser())

        #
        Progress = 30
        LoadWin.progressUpdate(Progress)
        LoadWin.textUpdate("Preparing...")
        # time.sleep(1)
        #

        # footer
        self.timer = QtCore.QTimer()
        now = datetime.datetime.now().strftime("%B %d, %Y  %H:%M:%S")
        self.ui.footerLabel.setText(now)
        self.timer.timeout.connect(
            lambda: self.update_time(self.ui.footerLabel))
        self.timer.start(1000)

        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.maximizeBtn.clicked.connect(
            lambda: self.handle_maximize())

        # Notification Center
        self.ui.notificationBtn.clicked.connect(
            lambda: self.handleNotificationPopup())

        # head bar
        self.ui.headerContainer.mousePressEvent = lambda event: self.mousePressEvent(
            event, header=True)
        self.ui.searchBox.textChanged.connect(
            lambda: self.search_query(self.ui.searchBox.text(),))

        # Dashboard Page
        self.prepare_dashboard()

        # Reports Page
        self.prepare_reports()

        # News Section
        self.prepare_news_section()

        # Hire Page
        self.ui.hireEmployeeBtn.clicked.connect(
            lambda: self.add_employee_to_the_record(self.ui.hireSectionNameLineEdit.text(),
                                                    self.ui.hireSectionLastNameLineEdit.text(),
                                                    self.ui.hireSectionAgeSpinBox.value(),
                                                    self.ui.hireSectionSalarySpinBox.value(),
                                                    self.ui.hireSectionPositionComboBox.currentText(),
                                                    self.ui.hireSectionEmailLineEdit.text()))

        # Card Section
        effect = QGraphicsDropShadowEffect(
            self.ui.personsCardContainer, enabled=True, blurRadius=5)
        self.ui.dashboardCardsContainer.setGraphicsEffect(effect)
        self.create_counter_animation(
            start=0, end=self.employees_number, label=self.ui.emoloyeeCounterLabel)
        self.create_counter_animation(
            start=0, end=avg_age(), label=self.ui.averageAgeCounterLabel)
        self.create_counter_animation(start=0, end=avg_salary(
        ), label=self.ui.averageSalaryCounterLabel, time=2)
        self.create_counter_animation(start=0, end=avg_salary(
        ), label=self.ui.averageSalaryCounterLabel, time=4)
        self.create_counter_animation(start=0, end=total_salary(
        ), label=self.ui.TotalSalaryCounterLabel, time=000000.1)

        # Dashboard Page Tables

        delegate = ReadOnlyDelegate(self)
        self.ui.salaryPositionTable.setItemDelegateForColumn(0, delegate)
        self.ui.salaryPositionTable.setItemDelegateForColumn(1, delegate)
        self.ui.employeePositionTable.setItemDelegateForColumn(0, delegate)
        self.ui.employeePositionTable.setItemDelegateForColumn(1, delegate)
        self.ui.avgAgePositionTable.setItemDelegateForColumn(0, delegate)
        self.ui.avgAgePositionTable.setItemDelegateForColumn(1, delegate)
        self.ui.top3AgeTable.setItemDelegateForColumn(0, delegate)
        self.ui.top3AgeTable.setItemDelegateForColumn(1, delegate)
        self.ui.top3SalaryTable.setItemDelegateForColumn(0, delegate)
        self.ui.top3SalaryTable.setItemDelegateForColumn(1, delegate)

        #
        Progress = 75
        LoadWin.progressUpdate(Progress)
        #

        # DataBase Page Table
        self.ui.filterByPositionComboBox.currentTextChanged.connect(
            lambda: self.on_filter_changed('position'))
        self.ui.filterBySalaryComboBox.currentTextChanged.connect(
            lambda: self.on_filter_changed('salary'))
        self.ui.tableWidget.setRowCount(self.employees_number)

        self.check_boxes = {}
        # populate table with data
        for q in range(self.employees_number):
            row = next(self.employees_generator)
            for j in range(len(row)):
                if j == 0:
                    check_box = QCheckBox(str(row[j]))
                    check_box.stateChanged.connect(
                        self.check_box_state_changed)
                    self.check_boxes[q] = {
                        'checkbox': check_box, 'text': f'{row[j]}'}
                    self.ui.tableWidget.setCellWidget(
                        q, j, check_box)
                else:
                    self.ui.tableWidget.setItem(
                        q, j, QTableWidgetItem(str(row[j]), ))

        self.ui.tableWidget.cellDoubleClicked.connect(
            self.display_update_query_popup)
        self.ui.tableWidget.setItemDelegateForColumn(0, delegate)
        self.ui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableWidget.customContextMenuRequested.connect(
            self.display_right_clicked_menu)

        # to hide the real headbar
        self.setWindowFlags(Qt.FramelessWindowHint)
        #
        LoadWin.textUpdate("Almost Done...")
        Progress = 100
        LoadWin.progressUpdate(Progress)
        # time.sleep(1)
        LoadWin.close()
        #
        self.show()

    def open_webbrowser(self):
        url = QUrl("https://github.com/ht21992")
        QDesktopServices.openUrl(url)

    def add_employee_to_the_record(self, emp_name, emp_lname, emp_age, emp_salary, emp_pos, emp_email):
        if '' in [emp_name, emp_lname, emp_age, emp_salary, emp_pos, emp_email]:
            self.display_popup(title="Error", msg="Please fill all the fields")
            return

        emp_id = str(random.choice(range(100, 999)))+emp_name[:2]+str(
            random.choice(range(100, 999)))+emp_lname[: 2]+str(random.choice(range(10, 99)))

        new_employee = create_employee_object(emp_id, emp_name, emp_lname, int(emp_age), int(emp_salary), emp_pos,
                                              emp_email)

        emp_sginal, employee_acceptance_msg = insert_data(new_employee)
        if emp_sginal:

            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            new_emp_check_box = QCheckBox(str(emp_id))
            new_emp_check_box.stateChanged.connect(
                self.check_box_state_changed)
            self.check_boxes[self.ui.tableWidget.rowCount(
            ) - 1] = {'checkbox': new_emp_check_box, 'text': f'{emp_id}'}
            self.ui.tableWidget.setCellWidget(
                self.ui.tableWidget.rowCount() - 1, 0, new_emp_check_box)
            for index, value in enumerate([emp_name, emp_lname, emp_age, emp_salary, emp_pos, emp_email], start=1):
                self.ui.tableWidget.setItem(
                    self.ui.tableWidget.rowCount() - 1, index, QTableWidgetItem(str(value), ))
            self.isChanged = True
            self.display_popup(
                title="Done", msg="Employee added successfully", color="#45B8AC")

        else:
            self.display_popup(title="Error", msg="Please check your inputs")

    def update_time(self, lbl):
        now = datetime.datetime.now()
        cur_time = now.strftime("%B %d, %Y  %H:%M:%S")
        lbl.setText(cur_time)

    def prepare_news_section(self):

        layout = QVBoxLayout(self.ui.newsContainer)
        scrollArea = QScrollArea()
        layout.setContentsMargins(0, 9, 0, 9)
        layout.addWidget(scrollArea)
        top_widget = QWidget()
        top_layout = QVBoxLayout()
        buttonGroup = QButtonGroup(top_widget)

        for i in range(self.news_number):
            news_id, news_title, news_content = next(self.news_generator)
            group_box = QGroupBox()
            group_box.setMinimumSize(180, 100)
            group_box.setMaximumSize(190, 16777215)
            group_box.setStyleSheet('background-color:#16191d')
            layout = QVBoxLayout(group_box)
            layout.addSpacing(6)
            layout.setContentsMargins(5, 5, 5, 7)
            label = QLabel()
            label.setWordWrap(True)
            label.setText(news_content[:150]+'...')

            title_btn = QPushButton(news_title)

            title_btn.setStyleSheet(
                'font-size:14px;font-weight:bold;color:#D65076;text-align: left')
            title_btn.setCursor(Qt.PointingHandCursor)

            buttonGroup.addButton(title_btn, i)

            layout.addWidget(title_btn)
            layout.addWidget(label)
            top_layout.addWidget(group_box)
        buttonGroup.idClicked.connect(self.display_news_popup)
        top_widget.setLayout(top_layout)
        scrollArea.setWidget(top_widget)
        # self.gridButtons[position[0]] [position[1]] = QPushButton(button, clicked = functools.partial(self.numberPressed, button))

    def display_news_popup(self, btnId):

        self.popupWindow = Popup()
        self.popupWindow.setFixedWidth(513)
        self.popupWindow.setFixedHeight(183)
        self.popupWindow.ui.popupTitleLabel.setText(self.news_list[btnId][1])
        self.popupWindow.ui.popupUpdateContainer.hide()
        self.popupWindow.ui.popupUpdateSubContainerQSpinBox.hide()

        self.popupWindow.ui.popupMessage.setText(self.news_list[btnId][2])
        self.popupWindow.ui.popupDoneBtn.hide()
        self.popupWindow.ui.popupIconLabel.hide()
        self.popupWindow.ui.popupTitleLabel.setStyleSheet(
            'font-size:16px;color:#D65076')
        self.popupWindow.show()

    def display_popup(self, title, msg, color="#D65076"):
        self.popupWindow = Popup()
        self.popupWindow.setFixedWidth(513)
        self.popupWindow.setFixedHeight(183)
        self.popupWindow.ui.popupTitleLabel.setText(title)
        self.popupWindow.ui.popupUpdateContainer.hide()
        self.popupWindow.ui.popupUpdateSubContainerQSpinBox.hide()
        self.popupWindow.ui.popupMessage.setText(msg)
        self.popupWindow.ui.popupDoneBtn.hide()
        self.popupWindow.ui.popupMessage.setStyleSheet(
            f'font-size:14px')
        self.popupWindow.ui.popupTitleLabel.setStyleSheet(
            f'font-size:16px;color:{color}')
        self.popupWindow.show()

    def prepare_reports(self):
        gantt_browser = QtWebEngineWidgets.QWebEngineView(
            self.ui.ganttChartContainer)
        gantt_browser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        def selector(x, y): return f'{x[y][1]} {x[y][2]}'

        df = pd.DataFrame(
            [
                dict(Task="Prototype", Start="2022-12-10",
                     Finish="2022-12-30", Resource=selector(display_table()[:], np.random.randint(10, size=1)[0])),
                dict(Task="Development", Start="2023-01-01",
                     Finish="2023-02-05", Resource=selector(display_table()[:], np.random.randint(10, size=1)[0])),
                dict(Task="Design", Start="2022-12-25",
                     Finish="2023-01-15", Resource=selector(display_table()[:], np.random.randint(10, size=1)[0])),
                dict(Task="Testing", Start="2023-01-07",
                     Finish="2023-02-02", Resource=selector(display_table()[:], np.random.randint(10, size=1)[0])),


            ]
        )
        df["Start"] = pd.to_datetime(df["Start"])
        df["Finish"] = pd.to_datetime(df["Finish"])

        ganttChart = px.timeline(df, x_start="Start", x_end="Finish",
                                 y="Task", color="Resource")

        progress_data = pd.DataFrame(
            {
                "Date": pd.date_range(
                    df.loc[:, ["Start", "Finish"]].values.min(),
                    df.loc[:, ["Start", "Finish"]].values.max(),
                    freq="W-MON",
                )
            }
        ).pipe(lambda d: d.assign(Value=np.random.randint(1, 20, len(d))))

        task_tracer_one = go.Scatter(
            x=progress_data.Date, y=progress_data.Value, name="Tasks Progress")

        fig = make_subplots(rows=2, cols=1, figure=ganttChart)
        fig.add_trace(task_tracer_one, row=2, col=1)

        fig.update_layout(xaxis1_showticklabels=True,
                          xaxis2_showticklabels=True)

        fig.update_layout(
            font_color="white",
            title="Tasks Reports",
            paper_bgcolor='#1f232a',
            plot_bgcolor='#1f232a'
        )

        config = {
            'displaylogo': False,

            'toImageButtonOptions': {
                'format': self.saveFormat,  # one of png, svg, jpeg, webp
                'filename': 'barChart',
                'height': 500,
                'width': 700,
                'scale': 1
            }

        }

        gantt_plot_html_format = fig.to_html(include_plotlyjs='cdn',
                                             config=config)
        gantt_plot_html_format = HTML + \
            gantt_plot_html_format[gantt_plot_html_format.find('body') + 5:]

        gantt_browser.setHtml(gantt_plot_html_format)

        self.ui.ganttChartVLayout.addWidget(gantt_browser)

    def prepare_dashboard(self):
        # Plot Section
        self.generate_bar_chart()
        # Pie Chart
        self.generate_pie_chart()
        # employeePositionTable
        self.populate_table(self.ui.employeePositionTable, self.emp_per_pos)
        # salaryPositionTable
        self.populate_table(self.ui.salaryPositionTable,
                            self.avg_salary_per_pos)

        # avgAgePositionTable
        self.populate_table(self.ui.avgAgePositionTable, self.avg_per_pos)

        # top3SalaryTable
        self.populate_table(self.ui.top3SalaryTable,
                            self.top_n_by_salaray, type='top3')

        # top3AgeTable
        self.populate_table(self.ui.top3AgeTable,
                            self.top_n_by_age, type='top3')

    def populate_table(self, table_widget, data, type='normal'):
        table_widget.setRowCount(len(data))
        if type == 'normal':
            for rIndex, (pos, counter) in enumerate(data):
                row = (pos, counter)
                for cIndex in range(len(row)):
                    item = QTableWidgetItem(str(row[cIndex]),)
                    item.setTextAlignment(Qt.AlignCenter)
                    table_widget.setItem(
                        rIndex, cIndex, item)
        else:
            for rIndex, (name, lname, salary) in enumerate(data):
                full_name = f"{name} {lname}"
                row = (full_name, salary)
                for cIndex in range(len(row)):
                    item = QTableWidgetItem(str(row[cIndex]),)
                    item.setTextAlignment(Qt.AlignCenter)
                    table_widget.setItem(
                        rIndex, cIndex, item)

    def check_box_state_changed(self):
        current_row = self.ui.tableWidget.currentRow()

        if self.check_boxes[current_row]['checkbox'].isChecked():
            self.rowsToDelete.append(
                (self.check_boxes[current_row]['text'], current_row))
        else:
            self.rowsToDelete.remove(
                (self.check_boxes[current_row]['text'], current_row))
        self.ui.deleteSelectedRowsBtn.show() if len(
            self.rowsToDelete) > 0 else self.ui.deleteSelectedRowsBtn.hide()

    def update_employee_table(self, table):
        self.ui.tableWidget.clearContents()
        gen = generator(table)
        for q in range(len(table)):
            row = next(gen)
            for j in range(len(row)):
                if j == 0:
                    check_box = QCheckBox(str(row[j]))
                    check_box.stateChanged.connect(
                        self.check_box_state_changed)
                    self.check_boxes[q] = {
                        'checkbox': check_box, 'text': f'{row[j]}'}
                    self.ui.tableWidget.setCellWidget(
                        q, j, check_box)
                else:
                    self.ui.tableWidget.setItem(
                        q, j, QTableWidgetItem(str(row[j]), ))

    def display_right_clicked_menu(self, pos):
        menu = QMenu()
        current_row = self.ui.tableWidget.currentRow()
        emp_id = self.check_boxes[current_row]['text']
        current_column = self.ui.tableWidget.currentColumn()
        current_item = self.ui.tableWidget.currentItem().text()
        delete_btn = menu.addAction('Delete Row')
        delete_btn.setIcon(QIcon("./images/delete.png"))
        delete_btn.triggered.connect(
            lambda: self.display_delete_query_popup(current_item, emp_id))
        update_btn = menu.addAction('Update Cell')
        update_btn.setIcon(QIcon("./images/update.png"))
        update_btn.triggered.connect(
            lambda: self.display_update_query_popup(current_row, current_column))
        menu.exec_(self.ui.tableWidget.mapToGlobal(pos))

    def display_update_query_popup(self, row, col, title='Update Employee Information'):

        self.popupWindow = Popup()
        self.popupWindow.setFixedWidth(513)
        self.popupWindow.setFixedHeight(183)
        try:
            cell_content = self.ui.tableWidget.currentItem().text()
        except AttributeError:
            return

        employee_id = self.check_boxes[row]['text']
        col_header = self.ui.tableWidget.horizontalHeaderItem(col).text()
        note = ''
        if col_header == "Position":
            self.popupWindow.ui.popupUpdateSubContainerQLineEdit.hide()
            self.popupWindow.ui.popupUpdateSubContainerQSpinBox.hide()
            self.popupWindow.ui.popupUpdateComboBox.setCurrentText(
                cell_content)
            self.popupWindow.ui.popupDoneBtn.clicked.connect(
                lambda: self.update_employee_information(col_header, self.popupWindow.ui.popupUpdateComboBox.currentText(), employee_id))
        else:
            if col_header in ['Age', "Salary"]:
                header_range = {'Age': (18, 70), 'Salary': (500, 10000), 'Suffix': {
                    'Age': " Years Old", "Salary": " $"}}
                self.popupWindow.ui.updateSpinBox.setRange(
                    header_range[col_header][0], header_range[col_header][1])
                note = f'{header_range[col_header][0]} < {col_header} < {header_range[col_header][1]}'
                self.popupWindow.ui.popupUpdateSubContainerQLineEdit.hide()
                self.popupWindow.ui.popupUpdateSubContainerComboBox.hide()
                self.popupWindow.ui.updateSpinBox.setValue(int(cell_content))
                self.popupWindow.ui.updateSpinBox.setSuffix(
                    header_range['Suffix'][col_header])
                self.popupWindow.ui.popupDoneBtn.clicked.connect(
                    lambda: self.update_employee_information(col_header, self.popupWindow.ui.updateSpinBox.value(), employee_id))

            else:
                self.popupWindow.ui.popupUpdateSubContainerQSpinBox.hide()
                self.popupWindow.ui.popupUpdateSubContainerComboBox.hide()
                self.popupWindow.ui.updateNameLineEdit.setText(cell_content)
                self.popupWindow.ui.popupDoneBtn.clicked.connect(
                    lambda: self.update_employee_information(col_header, self.popupWindow.ui.updateNameLineEdit.text(), employee_id))

        self.popupWindow.ui.popupTitleLabel.setText(
            f"Update {col_header} {'('+note+')' if note != '' else ''}")
        self.popupWindow.ui.popupMessageSubContainer.hide()

        self.popupWindow.show()

    def update_employee_information(self, col_header, new_value, employee_id):
        if col_header == 'Lastname':
            col_header = 'lname'
        if isinstance(new_value, str):
            if len(new_value) == 0:
                return
        update_employee(col_header, new_value, employee_id)
        self.ui.tableWidget.currentItem().setText(str(new_value))
        self.isChanged = True
        self.popupWindow.close()

    def display_delete_query_popup(self, emp_id='multi', del_value='multi', title='Delete Employee'):

        self.popupWindow = Popup()
        self.popupWindow.setFixedWidth(513)
        self.popupWindow.setFixedHeight(183)
        self.popupWindow.ui.popupTitleLabel.setText(title)
        self.popupWindow.ui.popupUpdateContainer.hide()
        if del_value == 'multi':
            self.popupWindow.ui.popupMessage.setText(
                f'Are you sure ? <b style="color:#DD4124">{len(self.rowsToDelete)}</b> employee(s) will be deleted')
            self.popupWindow.ui.popupDoneBtn.clicked.connect(
                lambda: self.remove_employee(emp_id='multi', field='emp_id'))
            self.popupWindow.show()
            return

        self.popupWindow.ui.popupMessage.setText(
            f'Are you sure about deleting <b style="color:#DD4124">{del_value}</b> ? The row with Employee ID '
            f'<b style="color:#DD4124">{emp_id}</b> will be deleted')
        self.popupWindow.ui.popupDoneBtn.clicked.connect(
            lambda: self.remove_employee(emp_id, 'emp_id'))
        self.popupWindow.show()

    def remove_employee(self, emp_id='multi', field='emp_id'):

        if emp_id == 'multi':
            for e_id, row in self.rowsToDelete:
                delete_employee(e_id, field)
            self.check_boxes = {}
            self.rowsToDelete.clear()
            self.update_employee_table(display_table())
            self.ui.deleteSelectedRowsBtn.hide()
            self.popupWindow.close()
            self.isChanged = True
            return

        delete_employee(emp_id, field)
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())
        self.isChanged = True
        self.popupWindow.close()

    def create_counter_animation(self, start, end, label, time=100):
        start = 0
        end = end
        timeLine = QTimeLine(abs(end - start)*time,
                             label)
        timeLine.setFrameRange(start, end)
        timeLine.frameChanged.connect(label.setNum)
        # set start value
        label.setNum(start)
        # start timer
        timeLine.start()

    def generate_pie_chart(self):
        pie_browser = QtWebEngineWidgets.QWebEngineView(
            self.ui.barChartContainer)
        # to accept downloads from QtWebEngineWidgets
        pie_browser.page().profile().downloadRequested.connect(_downloadRequested)
        pie_browser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        pie_browser.setStyleSheet("background-color:red")
        fig = go.Figure(data=go.Pie(values=[i[1] for i in self.emp_per_pos], labels=[i[0] for i in self.emp_per_pos],
                                    ))

        config = {
            'displaylogo': False,

            'toImageButtonOptions': {
                'format': self.saveFormat,
                'filename': 'pieChart',
                'height': 500,
                'width': 700,
                'scale': 1
            }

        }

        fig.update_traces(textposition='inside')
        fig.update_layout(
            font_color="white",
            paper_bgcolor='#1f232a',
            plot_bgcolor='#1f232a',
            uniformtext_minsize=12,
            uniformtext_mode='hide',
            legend=dict(font=dict(size=10, color="white")),
            legend_title_text='Employee/Position'

        )

        pie_plot_html_format = fig.to_html(
            include_plotlyjs='cdn', config=config)
        pie_plot_html_format = HTML + \
            pie_plot_html_format[pie_plot_html_format.find('body') + 5:]

        pie_browser.setHtml(pie_plot_html_format)

        self.ui.horizontalLayout_23.addWidget(pie_browser)

    def generate_bar_chart(self):
        bar_browser = QtWebEngineWidgets.QWebEngineView(
            self.ui.barChartContainer)
        bar_browser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        fig = go.Figure(data=go.Bar(x=[i[0] for i in self.avg_salary_per_pos], y=[i[1] for i in self.avg_salary_per_pos],
                                    marker={'color': ['red', 'purple', 'blue', 'green'],
                                            'colorscale': 'Viridis'}))
        fig.update_layout(
            font_color="white",
            title="Average Salary per Position Bar Plot",
            paper_bgcolor='#1f232a',
            plot_bgcolor='#1f232a'
        )

        config = {
            'displaylogo': False,

            'toImageButtonOptions': {
                'format': self.saveFormat,
                'filename': 'barChart',
                'height': 500,
                'width': 700,
                'scale': 1
            }



        }

        bar_plot_html_format = fig.to_html(include_plotlyjs='cdn',
                                           config=config)
        bar_plot_html_format = HTML + \
            bar_plot_html_format[bar_plot_html_format.find('body') + 5:]

        bar_browser.setHtml(bar_plot_html_format)

        self.ui.horizontalLayout_21.addWidget(bar_browser)

    def search_query(self, searched_text):
        self.ui.personnelBtn.click()
        searched_query = search_employee(searched_text, '*')
        self.ui.tableWidget.clearContents()
        if len(searched_query) > 0:
            gen = generator(searched_query)
            for q in range(len(searched_query)):
                row = next(gen)
                for j in range(len(row)):
                    if j == 0:
                        check_box = QCheckBox(str(row[j]))
                        check_box.stateChanged.connect(
                            self.check_box_state_changed)
                        self.check_boxes[q] = {
                            'checkbox': check_box, 'text': f'{row[j]}'}
                        self.ui.tableWidget.setCellWidget(
                            q, j, check_box)
                    else:
                        self.ui.tableWidget.setItem(
                            q, j, QTableWidgetItem(str(row[j]), ))

    def on_filter_changed(self, filter_name='position'):
        filter_dict = {'position': self.filter_by_position,
                       'salary': self.filter_by_salary}
        filter_dict.get(filter_name)()

    def find_min_and_max_vals(self, text):
        and_index = text.find('And')
        if and_index == -1:
            if text[0] == '>':
                min_value = int(text[1:])
                max_value = 100_000_000_000_000_000
            else:
                min_value = 0
                max_value = int(text[1:])
        else:

            gt_index = text.find('>')
            le_index = text.find('<')
            min_value = text[gt_index+1:and_index]
            max_value = text[le_index+1:]

        return int(min_value), int(max_value)

    def filter_by_salary(self):

        current_filter = self.ui.filterBySalaryComboBox.currentText()
        if current_filter == 'All Salaries':
            searched_query = search_employee('', 'position')
        else:
            min_value, max_value = self.find_min_and_max_vals(current_filter)
            searched_query = search_employee((min_value, max_value), 'salary')
        self.ui.tableWidget.clearContents()
        self.check_boxes = {}
        if len(searched_query) > 0:
            gen = generator(searched_query)
            for q in range(len(searched_query)):
                row = next(gen)
                for j in range(len(row)):
                    if j == 0:
                        check_box = QCheckBox(str(row[j]))
                        check_box.stateChanged.connect(
                            self.check_box_state_changed)
                        self.check_boxes[q] = {
                            'checkbox': check_box, 'text': f'{row[j]}'}
                        self.ui.tableWidget.setCellWidget(
                            q, j, check_box)
                    else:
                        self.ui.tableWidget.setItem(
                            q, j, QTableWidgetItem(str(row[j]), ))

    def filter_by_position(self):
        # self.ui.filterBySalaryComboBox.setCurrentIndex(0)
        current_filter = '' if self.ui.filterByPositionComboBox.currentText(
        ) == 'All Positions' else self.ui.filterByPositionComboBox.currentText()
        searched_query = search_employee(current_filter, 'position')
        self.ui.tableWidget.clearContents()
        self.check_boxes = {}
        if len(searched_query) > 0:
            gen = generator(searched_query)
            for q in range(len(searched_query)):
                row = next(gen)
                for j in range(len(row)):
                    if j == 0:
                        check_box = QCheckBox(str(row[j]))
                        check_box.stateChanged.connect(
                            self.check_box_state_changed)
                        self.check_boxes[q] = {
                            'checkbox': check_box, 'text': f'{row[j]}'}
                        self.ui.tableWidget.setCellWidget(
                            q, j, check_box)
                    else:
                        self.ui.tableWidget.setItem(
                            q, j, QTableWidgetItem(str(row[j]), ))

    def handle_maximize(self):
        if self.isMaximized():
            self.ui.maximizeBtn.setIcon(
                QIcon(f"./icons/{self.theme}/maximize.svg"))
            self.showNormal()
        else:
            self.ui.maximizeBtn.setIcon(
                QIcon(f"./icons/{self.theme}/minimize.svg"))
            self.showMaximized()

    def handleNotificationPopup(self):
        height = self.ui.popupNotificationContainer.height()
        self.animation = QPropertyAnimation(
            self.ui.popupNotificationContainer, b"maximumHeight")
        if height == 0:
            new_height = 100

        else:
            new_height = 0

        self.animation.setDuration(250)
        self.animation.setStartValue(height)
        self.animation.setEndValue(new_height)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def handleMainContent(self, index, btn):

        if index == 1 and self.isChanged:
            self.ui.emoloyeeCounterLabel.setText(str(len(display_table())))
            self.ui.averageAgeCounterLabel.setText(str(avg_age()))
            self.ui.averageSalaryCounterLabel.setText(str(avg_salary()))
            self.ui.TotalSalaryCounterLabel.setText(str(total_salary()))
            self.clearLayout(self.ui.horizontalLayout_21)
            self.clearLayout(self.ui.horizontalLayout_23)
            self.fetch_data()
            self.prepare_dashboard()
            self.isChanged = False

        btn.setStyleSheet(
            f'background-color:#1f232a')
        if self.previousClickedBtn:
            if btn is self.previousClickedBtn:
                pass
            else:
                self.previousClickedBtn.setStyleSheet(
                    f'background-color:#16191d')
                self.previousClickedBtn = btn

        if not self.previousClickedBtn:
            self.previousClickedBtn = btn

        self.ui.stackedWidget_3.setCurrentIndex(index)

    def handleSlideLeftMenu(self):
        width = self.ui.leftMenuContainer.width()
        self.animation = QPropertyAnimation(
            self.ui.leftMenuContainer, b"maximumWidth")
        if width > 47:
            new_width = 47
            self.ui.menuBtn.setIcon(QIcon(f"./icons/white/menu.svg"))
        else:
            new_width = 130
            self.ui.menuBtn.setIcon(
                QIcon(f"./icons/white/align-justify.svg"))

        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def handleSlideCenterMenu(self, index=1, centerTitle=""):
        width = self.ui.centerMenuContainer.width()

        if index == -1:
            new_width = 0

        else:
            self.ui.stackedWidget.setCurrentIndex(index)

            new_width = 250

        self.animation = QPropertyAnimation(
            self.ui.centerMenuContainer, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        self.ui.centerMenuLabel.setText(centerTitle)

    def handleSlideRightMenu(self, index=1):
        width = self.ui.rightMenuContainer.width()

        if index == -1:
            new_width = 0

        else:
            self.ui.rightMenuLabel.setText(
                "My Profile" if index == 0 else "More")
            self.ui.stackedWidget_2.setCurrentIndex(index)
            new_width = 260

        self.animation = QPropertyAnimation(
            self.ui.rightMenuContainer, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event, header=False):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
            self.header = header
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        try:
            if not self.isMaximized() and self.header and self.offset is not None and event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.pos() - self.offset)
            else:
                super().mouseMoveEvent(event)
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    LoadWin = LoadingWindow()
    app.processEvents()
    window = MainWindow()
    sys.exit(app.exec_())
