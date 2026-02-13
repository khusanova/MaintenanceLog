//
//  Item.swift
//  MaintenanceLog
//
//  Created by Y. Khusanova on 13.02.26.
//

import Foundation
import SwiftData

@Model
final class Item {
    var timestamp: Date
    
    init(timestamp: Date) {
        self.timestamp = timestamp
    }
}
