//
//  LogEntry.swift
//  MaintenanceLog
//
//  Created by Y. Khusanova on 13.02.26.
//

import Foundation
import SwiftData

enum AlertColor: String, Codable{
    case green
    case yellow
    case red
    case infrared
}

@Model
final class LogEntry {
    var dateLast: Date
    var dateNext: Date
    var content: String
    var frequency: Int
    var urgencyState: AlertColor
    
    init(content: String, frequency: Int){
        self.content = content
        self.frequency = frequency
        self.dateLast = Date()
        self.urgencyState = AlertColor.green
        self.dateNext = Calendar.current.date(byAdding: DateComponents(day: frequency), to: Date()) ?? Date()
    }
}

extension LogEntry {
    static let waterPlants = LogEntry(content: "Water plants", frequency: 7)
    static let cleanDishWasherFilter = LogEntry(content: "Clean dish washer filter", frequency: 28)
    static let vacuum = LogEntry(content: "Vacuum", frequency: 7)
}
